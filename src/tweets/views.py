from django.shortcuts import render, get_object_or_404 
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Tweet
from .forms import TweetModelForm
from .mixin import FormUserNeededMixin,UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()

class TweetListView(ListView):

    def get_queryset(self, *args, **kwargs):

        queryset = Tweet.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            queryset = queryset.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return queryset

    def get_context_data(self, *args, **kwargs):
      context = super(TweetListView, self).get_context_data(*args, **kwargs)
      return context

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'


class TweetDeleteView(DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweet:list')
