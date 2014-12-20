from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Stream(models.Model):
    # Each nation must have a user.
    user = models.OneToOneField(User)

    stream_title = models.CharField(max_length=240, default='Untitled Broadcast')
    stream_description = models.CharField(max_length=240, default='')
    stream_game = models.CharField(max_length=240, default="No Game Selected")
    stream_team = models.CharField(max_length=240, default="No Team")
    stream_online = models.BooleanField(default=False)