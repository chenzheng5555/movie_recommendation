from itertools import count
import math
from statistics import mode
from django.http import JsonResponse
from . import models
import json
from django.db.models import Avg, Max, Min, Count, Sum
from django.db.models import F, Q


def get_genres_list(request):
    data = models.Genre.objects.values('g_id', 'g_name')
    return JsonResponse({'code': 0, 'data': list(data), 'msg': '成功'})


def get_country_list(request):
    data = models.Country.objects.values('c_id', 'c_name')
    return JsonResponse({'code': 0, 'data': list(data), 'msg': '成功'})


def get_filmtime_list(request):
    data = models.Movie.objects.values('filming_time').order_by('filming_time').distinct()
    return JsonResponse({'code': 0, 'data': list(data), 'msg': '成功'})


def get_film_list(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        g_id = json_data.get('g_id')
        c_id = json_data.get('c_id')
        offset = json_data.get('offset')
        limit = json_data.get('limit')
        #print(g_id, c_id, offset, limit)

    if g_id == -1 and c_id == -1:
        data = models.Movie.objects.values()
        total = len(data)
        #print(total, data)
        return JsonResponse({'code': 0, 'data': {'list': list(data[offset:offset + limit]), 'total': total}, 'msg': '成功'})

    mids = None
    if g_id != -1:
        mids = models.MovieGenre.objects.filter(g_id=g_id).values('m_id')
    if c_id != -1:
        mids1 = models.MovieCountry.objects.filter(c_id=c_id).values('m_id')
        if mids:
            mids = mids.filter(m_id__in=mids1)
        else:
            mids = mids1

    data = models.Movie.objects.filter(m_id__in=mids).values()
    total = len(data)

    return JsonResponse({'code': 0, 'data': {'list': list(data[offset:offset + limit]), 'total': total}, 'msg': '成功'})


def get_country_by_id(request):
    m_id = request.GET.get('m_id')
    if not m_id:
        return JsonResponse({'code': 100, 'data': {}, 'msg': '缺少参数'})

    ids = models.MovieCountry.objects.filter(m_id=m_id).values('c_id')
    data = models.Country.objects.filter(c_id__in=ids).values_list('c_name')

    return JsonResponse({'code': 0, 'data': list(data), 'msg': '成功'})


def get_genres_by_id(request):
    m_id = request.GET.get('m_id')
    if not m_id:
        return JsonResponse({'code': 100, 'data': {}, 'msg': '缺少参数'})

    ids = models.MovieGenre.objects.filter(m_id=m_id).values('g_id')
    data = models.Genre.objects.filter(g_id__in=ids).values_list('g_name')

    return JsonResponse({'code': 0, 'data': list(data), 'msg': '成功'})


def get_actors_by_id(request):
    m_id = request.GET.get('m_id')
    if not m_id:
        return JsonResponse({'code': 100, 'data': {}, 'msg': '缺少参数'})

    ids = models.MovieActor.objects.filter(m_id=m_id).values('a_id')
    data = models.Actor.objects.filter(a_id__in=ids).values_list('a_name')

    return JsonResponse({'code': 0, 'data': list(data), 'msg': '成功'})


def get_directors_by_id(request):
    m_id = request.GET.get('m_id')
    ids = models.MovieDirector.objects.filter(m_id=m_id).values('d_id')
    data = models.Director.objects.filter(d_id__in=ids).values_list('d_name')
    return JsonResponse({'code': 0, 'data': list(data), 'msg': '成功'})


def get_tags_by_id(request):
    m_id = request.GET.get('m_id')
    u_id = request.COOKIES.get('u_id')
    #print(m_id, u_id)
    tag_count = models.UserMovieTag.objects.filter(m_id=m_id).values('t_id').annotate(count=Count('*'), title=F('t__t_name'))
    u_tags = tag_count.filter(u_id=u_id).values('t_id')
    u_tag_count = tag_count.filter(t_id__in=u_tags).order_by('-count').values('title', 'count')
    o_tag_count = tag_count.exclude(t_id__in=u_tags).order_by('-count').values('title', 'count')

    return JsonResponse({'code': 0, 'data': {'user_tags': list(u_tag_count), 'other_tags': list(o_tag_count)}, 'msg': '成功'})


def add_user_movie_tag(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        m_id = json_data.get('m_id')
        t_name = json_data.get('t_name')
    u_id = request.COOKIES.get('u_id')

    tag = models.Tag.objects.filter(t_name=t_name)
    if len(tag) == 0:  # tag不存在
        t_id = models.Tag.objects.create(t_name=t_name).t_id
    elif len(tag) == 1:  # tag存在
        t_id = tag[0].t_id
    else:
        return JsonResponse({'code': 200, 'data': {}, 'msg': f'存在{len(tag)}个重复tag'})

    n = models.UserMovieTag.objects.filter(u_id=u_id, m_id=m_id, t_id=t_id)
    if len(n) == 0:  # 不存在相同标注记录
        umt = models.UserMovieTag.objects.create(u_id=u_id, m_id=m_id, t_id=t_id)
    count = models.UserMovieTag.objects.filter(m_id=m_id, t_id=t_id).count()
    return JsonResponse({'code': 0, 'data': {'count': count}, 'msg': '添加成功'})


def delete_user_movie_tag(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        m_id = json_data.get('m_id')
        t_name = json_data.get('t_name')
    u_id = request.COOKIES.get('u_id')

    t_id = models.Tag.objects.filter(t_name=t_name).first().t_id
    models.UserMovieTag.objects.filter(u_id=u_id, m_id=m_id, t_id=t_id).delete()
    n = models.UserMovieTag.objects.filter(t_id=t_id)
    if len(n)==0: #记录中的标签已经删除完
        models.Tag.objects.filter(t_id=t_id).delete()
    count = models.UserMovieTag.objects.filter(m_id=m_id, t_id=t_id).count()
    return JsonResponse({'code': 0, 'data': {'count': count}, 'msg': '删除成功'})



def get_user_movie_hist(request):
    u_id = request.COOKIES.get('u_id')
    u_movies = models.UserMovieHistory.objects.filter(u_id=u_id)
    #print(list(u_movies.values_list('m__title')))
    data =[]
    for i in range(1,5):
        movie = u_movies.filter(attr_id=i).order_by('attr_score')\
            .annotate(name=F('m__title'),value=F('attr_score')).values('name','value')
        data.append(list(movie))
    
    return JsonResponse({'code': 0, 'data': data, 'msg': '成功'})

def get_user_tag_hist(request):
    u_id = request.COOKIES.get('u_id')
    u_tags = models.UserTagHistory.objects.filter(u_id=u_id)
    #print(list(u_tags.values_list('t__t_name')))
    data =[]
    for i in range(1,5):
        tag = u_tags.filter(attr_id=i).order_by('attr_score')\
            .annotate(name=F('t__t_name'),value=F('attr_score')).values('name','value')
        data.append(list(tag))
    return JsonResponse({'code': 0, 'data': data, 'msg': '成功'})
