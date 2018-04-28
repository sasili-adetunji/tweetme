from django.views.generic.base import RedirectView

from .views import (
    TweetListAPIView, 
    TweetCreateAPIView
)
from django.conf.urls import url

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/')), # /tweet
    # url(r'^search/$', TweetListView.as_view(), name='list'), # /tweet
    url(r'^$', TweetListAPIView.as_view(), name='list'),  # api/tweet
    url(r'^create/$', TweetCreateAPIView.as_view(), name='create'),  # api/tweet/create
    # url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'), # /tweet/1/ 
    # url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'), # /tweet/1/ 
    # url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'), # /tweet/1/ 


]
