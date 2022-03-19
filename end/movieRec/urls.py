"""movieRec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from testdb import user,movie

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',user.login),
    path('register',user.register),
    path('get_rec_list', user.get_rec_list),
    path('get_user_info', user.get_user_info),
    path('change_password', user.change_password),
    path('forget_password', user.forget_password),

    path('get_genres_list', movie.get_genres_list),
    path('get_country_list', movie.get_country_list),
    path('get_filmtime_list', movie.get_filmtime_list),
    path('get_film_list', movie.get_film_list),
    path('send_email', user.send_email),

    path('get_actors_by_id', movie.get_actors_by_id),
    path('get_country_by_id', movie.get_country_by_id),
    path('get_genres_by_id', movie.get_genres_by_id),
    path('get_directors_by_id', movie.get_directors_by_id),
    path('get_tags_by_id', movie.get_tags_by_id),
    path('add_user_movie_tag', movie.add_user_movie_tag),
    path('delete_user_movie_tag', movie.delete_user_movie_tag),
    path('get_user_movie_hist', movie.get_user_movie_hist),
    path('get_user_tag_hist', movie.get_user_tag_hist),
    
    path('', TemplateView.as_view(template_name='index.html')),
] 
