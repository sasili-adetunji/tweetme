from django.db import models
from django.conf import settings
# Create your models here.

class UserProfile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
  # user.profile
  following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')
  # user.profile.following ---user I follow
  # user.follwed_by --- users that follw me --reverse reationship

  def __str__(self):
    return str(self.following.all().count())

