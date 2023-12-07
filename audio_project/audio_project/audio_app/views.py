# audio_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, AudioUploadForm, AudioChangeForm
from .models import AudioFile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

# @login_required
def upload_audio(request):
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)
        if form.is_valid():
            audio = form.save(commit=False)
            audio.user = request.user
            audio.save()
            return redirect('audio_list')
    else:
        form = AudioUploadForm()
    return render(request, 'audio_app/upload_audio.html', {'form': form})

@login_required
def audio_list(request):
    audio_files = AudioFile.objects.filter(user=request.user)
    return render(request, 'audio_app/audio_list.html', {'audio_files': audio_files})

@login_required
def change_audio(request, audio_id):
    audio = AudioFile.objects.get(id=audio_id, user=request.user)
    if request.method == 'POST':
        form = AudioChangeForm(request.POST, request.FILES, instance=audio)
        if form.is_valid():
            form.save()
            return redirect('audio_list')
    else:
        form = AudioChangeForm(instance=audio)
    return render(request, 'audio_app/change_audio.html', {'form': form})
