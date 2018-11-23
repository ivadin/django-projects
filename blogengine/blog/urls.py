from django.conf.urls import url, include
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^$', posts_list, name='posts_list_url'),
    url(r'^post/create/$', PostCreate.as_view(), name='post_create_url'),
    url(r'^post/(?P<slug>.+)/update/$', PostUpdate.as_view(), name='post_update_url'),
    url(r'^post/(?P<slug>.+)/$', PostDetail.as_view(), name='post_detail_url'),
    url(r'^tags/$', tags_list, name='tags_list_url'),
    url(r'^tag/create/$', TagCreate.as_view(), name='tag_create_url'),
    url(r'^tag/(?P<slug>.+)/update/$', TagUpdate.as_view(), name='tag_update_url'),
    url(r'^tag/(?P<slug>.+)/$', TagDetail.as_view(), name='tag_detail_url'),
]
