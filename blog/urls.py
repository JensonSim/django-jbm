from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    #post로 시작해야 하고 /가 들어가야함 그리고 장고가 pk번호를 집어넣어주고 그 번호는 숫자로 나와야함 자리수는 늘어날수 있음 
    # 다시 슬래쉬가 들어가야 하고 끝나야됨 더있으면 안됩니다. 
    #그리고 이 조건을 만족하는 경우에는 ,  views.py의 post_detail을 호출하고 지시에 따른다. 
]