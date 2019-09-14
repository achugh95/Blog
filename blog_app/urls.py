"""
URLs for the blog_app
"""

from django.conf.urls import url
from . import views                 # Importing all the views which will be mapped to respective URLs

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='list_all_posts'),
    url(r'^blog/(?P<pk>\d+)/', views.PostDetail.as_view(), name='detail_post'),
    url(r'^CreatePost/', views.create_post, name='create_post'),
    url(r'^EditPost/(?P<pk>\d+)/', views.edit_post, name='edit_post'),
]
