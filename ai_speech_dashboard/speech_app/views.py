import os
import speech_recognition as sr

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import AudioUpload
from .forms import AudioUploadForm


# =========================
# 🔊 TRANSCRIBE FUNCTION
# =========================
def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    full_text = ""

    try:
        with sr.AudioFile(file_path) as source:
            duration = source.DURATION
            offset = 0
            chunk_duration = 50  # seconds

            while offset < duration:
                audio = recognizer.record(source, duration=chunk_duration)

                try:
                    text = recognizer.recognize_google(audio)
                    full_text += text + " "
                except sr.UnknownValueError:
                    pass
                except sr.RequestError:
                    return "Speech API unavailable"

                offset += chunk_duration

        return full_text.strip()

    except Exception as e:
        return f"Error processing audio: {str(e)}"


# =========================
# 📤 UPLOAD VIEW
# =========================
def upload_audio(request):
    if request.method == 'POST':
        form = AudioUploadForm(request.POST, request.FILES)

        if form.is_valid():
            upload = form.save(commit=False)

            # temporary save
            upload.transcription = "Processing..."
            upload.save()

            file_path = upload.audio_file.path

            # transcribe
            transcription = transcribe_audio(file_path)

            # count words
            word_count = len(transcription.split()) if transcription else 0

            # update
            upload.transcription = transcription
            upload.word_count = word_count
            upload.save()

            messages.success(request, "Audio processed successfully!")

            return redirect('dashboard')

        else:
            messages.error(request, "❌ Please fix the errors below.")

    else:
        form = AudioUploadForm()

    return render(request, 'speech_app/upload.html', {'form': form})


# =========================
# 📊 DASHBOARD
# =========================
def dashboard(request):
    all_uploads = AudioUpload.objects.all()

    total_uploads = all_uploads.count()
    total_words = sum(upload.word_count for upload in all_uploads)

    return render(request, 'speech_app/dashboard.html', {
        'uploads': all_uploads,
        'total_uploads': total_uploads,
        'total_words': total_words,
    })


# =========================
# 📄 DETAIL VIEW
# =========================
def detail(request, pk):
    upload = get_object_or_404(AudioUpload, pk=pk)

    return render(request, 'speech_app/detail.html', {
        'upload': upload
    })


# =========================
# 🗑 DELETE VIEW
# =========================
def delete_upload(request, pk):
    upload = get_object_or_404(AudioUpload, pk=pk)

    if request.method == "POST":
        # delete file from storage
        if upload.audio_file and os.path.exists(upload.audio_file.path):
            os.remove(upload.audio_file.path)

        # delete DB record
        upload.delete()

        messages.success(request, "Recording deleted successfully!")
        return redirect('dashboard')

    return redirect('detail', pk=pk)