from django.shortcuts import render, get_object_or_404 
from django.urls import reverse_lazy
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
    # queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    success_url = '/tweet/create/'
    # login_url = '/admin/'

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    # template_name = 'tweets/detail_view.html'

    # def get_object(self):
        # print(self.kwargs)
        # pk = self.kwargs.get ('pk')
        # obj = get_object_or_404(Tweet, pk=pk)

        # print(pk)
        # return obj

class TweetListView(ListView):
    # template_name = 'tweets/list_view.html'
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
      context = super(TweetListView, self).get_context_data(*args, **kwargs)

      return context

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'tweets/update_view.html'
    success_url = '/tweet/'


class TweetDeleteView(DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('home')



# def tweet_create_view(request):
#     form = TweetModelForm(request.POST or None)
#     if form.is_valid():
#         instance = form.save(commit=False)
#         instance.user = request.user
#         instance.save()
#     context = {
#         'form': form
#     }
#     return render(request, 'tweets/create_view.html', context)


# def tweet_detail_view(request, pk=None):
# #   obj = Tweet.objects.get(pk=pk)
#   obj = get_object_or_404(Tweet, pk=pk)
#   context = {
#     'object': obj
#   }
#   return render(request, 'tweets/detail_view.html', context )

# def tweet_list_view(request):
#   queryset = Tweet.objects.all()
#   for i in queryset:
#     print(i.content)
#   context = {
#     'object_list':queryset
#   }
#   return render(request, 'tweets/list_view.html', context)