from django.conf.urls import url
from pdown import views


urlpatterns = [
    url(r'^$', views.Posts.as_view(), name="posts"),
    url(r'^create/$', views.CreatePost.as_view(), name="create"),
    url(r'^update/(?P<id>\d+)/$', views.UpdatePost.as_view(), name="update"),
]