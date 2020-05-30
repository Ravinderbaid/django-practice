from django.conf.urls import url

from .views import (
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,
    # CommentEditAPIView,
    )

urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<id>\d+)/$', CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<id>\d+)/edit/$', CommentEditAPIView.as_view(), name='edit'),
    # url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
