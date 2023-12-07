# audio_app/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional user-related fields here

class AudioFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio/')
    # Add any additional audio-related fields here
