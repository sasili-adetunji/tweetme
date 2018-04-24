from .views import (
    TweetDetailView,
    TweetListView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView 
    )
from django.conf.urls import url

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list'), # /tweet
    url(r'^create/$', TweetCreateView.as_view(), name='create'),  # /tweet/create
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/ 
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/ 
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/ 


]
