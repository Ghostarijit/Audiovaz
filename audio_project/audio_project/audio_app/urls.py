# audio_app/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, upload_audio, audio_list, change_audio

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='registration/login.html', success_url='accounts/upload/'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('upload/', upload_audio, name='upload_audio'),
    path('audio-list/', audio_list, name='audio_list'),
    path('change_audio/<int:audio_id>/', change_audio, name='change_audio'),
]
