from django.conf.urls import url
from . import views
import django.contrib.auth.views
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout, name='logout',
        kwargs={'next_page': '/'}),
    url(r'^accounts/profile/$', views.user_detail, name='profile'),
    url(r'^accounts/edit/$', views.user_edit, name='user_edit'),
]
