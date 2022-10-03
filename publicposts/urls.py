from django.contrib import admin
from django.urls import path, re_path
from publicpostsapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/posts', views.posts),
    re_path(r'^api/like_post/(?P<post_id>[0-9]+)$', views.like_post),
    re_path(r'^api/delete_post/(?P<post_id>[0-9]+)$', views.delete_post)
]
