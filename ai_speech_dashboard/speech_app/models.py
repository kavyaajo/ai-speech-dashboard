"""
models.py — Where you define your DATABASE TABLES using Python classes.

In Django, a "Model" = a database table.
Each attribute of the class = a column in that table.

We only need ONE model (table) for this project: AudioUpload.
It stores everything about each uploaded audio file.

After editing models.py, you MUST run:
  python manage.py makemigrations   ← creates the migration file (a blueprint)
  python manage.py migrate          ← applies the blueprint to the actual DB

Think of migrations like Git commits for your database schema.
"""

from django.db import models


class AudioUpload(models.Model):
    """
    This class maps to a table called: speech_app_audioupload
    (Django auto-prefixes with app name)

    Columns this table will have:
    ┌─────────────────┬──────────────────────────────────────────┐
    │ Column          │ What it stores                           │
    ├─────────────────┼──────────────────────────────────────────┤
    │ id              │ Auto-created unique number for each row  │
    │ title           │ A name/label the user gives the upload   │
    │ audio_file      │ Path to the uploaded audio file          │
    │ transcription   │ The speech-to-text result                │
    │ word_count      │ How many words in the transcription      │
    │ uploaded_at     │ Timestamp when it was uploaded           │
    └─────────────────┴──────────────────────────────────────────┘
    """

    # CharField = text with a max length
    title = models.CharField(
        max_length=200,
        help_text="A label for this recording, e.g. 'Meeting Notes'"
    )

    # FileField = stores a file upload. upload_to= sets the subfolder inside MEDIA_ROOT
    # So files go to: media/uploads/your_audio.wav
    audio_file = models.FileField(
        upload_to='uploads/',
        help_text="The uploaded .wav or .mp3 file"
    )

    # TextField = long text with no character limit (perfect for transcriptions)
    # blank=True → allowed to be empty (in case transcription fails)
    transcription = models.TextField(
        blank=True,
        help_text="The speech-to-text result"
    )

    # IntegerField = whole numbers
    # default=0 → starts at zero before we calculate it
    word_count = models.IntegerField(
        default=0,
        help_text="Number of words in the transcription"
    )

    # DateTimeField with auto_now_add=True → automatically sets to NOW when created
    # You never need to set this manually — Django handles it!
    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When this file was uploaded"
    )

    def __str__(self):
        """
        __str__ controls how this object looks when printed.
        Example: "Meeting Notes (2024-01-15 10:30)"
        This also appears in the Django Admin panel.
        """
        return f"{self.title} ({self.uploaded_at.strftime('%Y-%m-%d %H:%M')})"

    class Meta:
        # Order results by newest first when fetching from DB
        ordering = ['-uploaded_at']
