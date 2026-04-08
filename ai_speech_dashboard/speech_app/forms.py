"""
forms.py — Django Forms handle user input safely.

Instead of manually reading request.POST data (error-prone),
Django Forms do the heavy lifting:
  ✅ Validate input automatically
  ✅ Show error messages
  ✅ Protect against malicious input

ModelForm = a Form that's directly tied to a Model.
We tell it which model and which fields to show.
"""

from django import forms
from .models import AudioUpload


class AudioUploadForm(forms.ModelForm):
    """
    This form will render two fields in our HTML:
    1. Title (text input)
    2. Audio file (file upload button)
    """

    class Meta:
        model = AudioUpload          # Tied to the AudioUpload model
        fields = ['title', 'audio_file']  # Only show these two fields

        # widgets let you customize how each field looks in HTML
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'e.g. Team Meeting, Lecture Notes...',
            }),
            'audio_file': forms.FileInput(attrs={
                'class': 'form-file',
                'accept': '.wav,.mp3',  # Only allow audio files in file picker
            }),
        }

        # Custom labels (the text shown above each field)
        labels = {
            'title': 'Recording Title',
            'audio_file': 'Audio File (.wav or .mp3)',
        }
