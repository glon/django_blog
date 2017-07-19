from django.conf.urls import url
from . import views

from django.conf import  settings

from django.contrib.auth import  views as auth_views

urlpatterns = [
    #url(r'^login/$', views.user_login, name='user_login'), # 自定义登录
    url(r'^login/$', auth_views.login, name='user_login'), # django 内置登录
    #url(r'^logout/$', auth_views.logout, name='user_logout'), # django 内置退出
    url(r'^logout/$', auth_views.logout, {'template_name':"account/logout.html"}, name='user_logout'), # django 内置退出
    url(r'^register/$', views.register,name='user_register'),
    url(r'^password-change/$', auth_views.password_change, {'post_change_redirect':'/account/password-change-done'}, name='password_change'),
    url(r'^password-change-done/$', auth_views.password_change_done, name='password_change_done'),
]
