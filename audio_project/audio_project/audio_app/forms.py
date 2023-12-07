# audio_app/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AudioFile
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class AudioUploadForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ('audio_file',)

class AudioChangeForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ('audio_file',)
