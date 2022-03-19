import email
from django.http import JsonResponse
from sqlalchemy import false, true
from . import models
import json
from django.core.mail import send_mail, send_mass_mail, EmailMultiAlternatives
import random


def login(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        u_name = json_data.get('u_name')
        password = json_data.get('password')

    user = models.User.objects.filter(u_name=u_name)
    if not (u_name and password):
        return JsonResponse({'code': 400, 'data': {}, 'msg': '参数为空'})

    if len(user) == 0:
        return JsonResponse({'code': 100, 'data': {}, 'msg': '用户不存在'})
    elif user[0].password != password:
        return JsonResponse({'code': 101, 'data': {}, 'msg': '密码错误'})

    rep = JsonResponse({'code': 0, 'data': {}, 'msg': '成功'})
    # domain = request.get_host()
    # print(domain)
    rep.set_cookie('u_id', user[0].u_id, domain="127.0.0.1", httponly=False, secure=True, samesite='None')
    return rep


def register(request):
    #print(request, json.loads(request.body))
    if request.method == 'POST':
        json_data = json.loads(request.body)
        u_name = json_data.get('u_name')
        email = json_data.get('email')
        password = json_data.get('password')

    #print(u_name, email, password)
    if not (u_name and email and password):
        return JsonResponse({'code': 400, 'data': {}, 'msg': '参数为空'})

    user = models.User.objects.filter(u_name=u_name)
    if len(user) >= 1:
        return JsonResponse({'code': 100, 'data': {}, 'msg': '用户已存在'})

    user = models.User(u_name=u_name, email=email, password=password)
    user.save()
    return JsonResponse({'code': 0, 'data': {}, 'msg': '成功'})


def get_rec_list(request):
    u_id = request.COOKIES.get('u_id')
    mids = models.RecommendMovie.objects.filter(u_id=u_id).order_by('ranking').values('m_id')
    #print(mids)

    data = models.Movie.objects.filter(m_id__in=mids).values()
    total = len(data)
    return JsonResponse({'code': 0, 'data': {'list': list(data), 'total': total}, 'msg': '成功'})


def get_user_info(request):
    u_id = request.COOKIES.get('u_id')
    if not u_id:
        return JsonResponse({'code': 102, 'data': {}, 'msg': 'cookie错误'})
    data = models.User.objects.get(u_id=u_id)
    if data:
        return JsonResponse({'code': 0, 'data': {'userId': data.u_id, 'userName': data.u_name}, 'msg': '成功'})
    return JsonResponse({'code': 101, 'data': {}, 'msg': '用户不存在'})


def change_password(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        password = json_data.get('password')
        new_password = json_data.get('newPassword')
    u_id = request.COOKIES.get('u_id')

    user = models.User.objects.filter(u_id=u_id)
    if len(user) == 0:
        return JsonResponse({'code': 100, 'data': {}, 'msg': '用户不存在'})
    elif user[0].password != password:
        return JsonResponse({'code': 101, 'data': {}, 'msg': '密码错误'})

    user.update(password=new_password)
    return JsonResponse({'code': 0, 'data': {}, 'msg': '成功'})


def forget_password(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        u_name = json_data.get('u_name')
        code = json_data.get('code')
        new_password = json_data.get('newPassword')
    #print(u_name, code, new_password)
    ucode = models.UserCode.objects.filter(u_name=u_name)
    if len(ucode) == 0:
        return JsonResponse({'code': 100, 'data': {}, 'msg': '用户不存在'})
    elif ucode[0].code != code:
        return JsonResponse({'code': 101, 'data': {}, 'msg': '验证码错误'})

    user = models.User.objects.filter(u_name=u_name)
    #print(user)
    user.update(password=new_password)
    return JsonResponse({'code': 0, 'data': {}, 'msg': '成功'})


def get_random_code(n):
    code = ""
    for i in range(n):
        code += str(random.randint(0, 9))
    return code


def send_email(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        u_name = json_data.get('u_name')
        email = json_data.get('email')

    if not (u_name and email):
        return JsonResponse({'code': 400, 'data': {}, 'msg': '参数为空'})

    user = models.User.objects.filter(u_name=u_name)
    if email != user[0].email:
        return JsonResponse({'code': 100, 'data': {}, 'msg': '邮箱错误'})

    code = get_random_code(6)
    emailmsg = "你正在修改你在基于标签的电影推荐平台中的密码，验证码为：" + code
    try:
        n = send_mail('验证码', emailmsg, from_email=None, recipient_list=[email])
    except:
        n = 0

    if n == 0:
        return JsonResponse({'code': 500, 'data': {}, 'msg': '邮件发送失败'})

    ucode = models.UserCode.objects.filter(u_name=u_name)
    if len(ucode) == 0:
        models.UserCode.objects.create(u_name=u_name, code=code)
    else:
        ucode.update(code=code)
    return JsonResponse({'code': 0, 'data': {}, 'msg': '验证码发送成功'})
