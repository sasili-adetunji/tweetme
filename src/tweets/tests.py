from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from django.contrib.auth import get_user_model
from .models import Tweet

User = get_user_model()

class TweetModelTestCAse(TestCase):
  def setUp(self):
    random_user = User.objects.create(username='randomtester')

  def test_tweet_item(self):
    obj = Tweet.objects.create(
      user= User.objects.first(),
      content='Some random contents'
    )
    self.assertTrue(obj.content == 'Some random contents')
    self.assertTrue(obj.id == 1)
    absolute_url = reverse('tweet:detail', kwargs={'pk': 1})
    self.assertEqual(obj.get_absolute_url(), absolute_url)

  def test_tweet_url(self):
    obj = Tweet.objects.create(
      user= User.objects.first(),
      content='Some random contents'
    )
    absolute_url = reverse('tweet:detail', kwargs={'pk': obj.pk})
    self.assertEqual(obj.get_absolute_url(), absolute_url)