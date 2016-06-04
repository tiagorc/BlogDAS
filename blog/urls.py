from django.conf.urls import include, url
from . import views
import django.contrib.auth.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^accounts/profile/$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
]
