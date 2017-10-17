from django.conf.urls import include, url
from django.confrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail'),
    url(r'^(?P<pk>\d+)/comments/new/$', 'main.vies.comment_new'),
]