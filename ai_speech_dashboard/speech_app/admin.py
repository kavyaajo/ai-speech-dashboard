"""
admin.py — Registers your models with Django's built-in Admin panel.

Once registered, you get a FREE admin interface at /admin/ where you can:
  - View all uploaded records
  - Edit or delete any record
  - Search and filter records

Zero extra code needed — Django generates the UI automatically!

To access admin:
  python manage.py createsuperuser
  → Enter username, email, password
  → Visit /admin/ in browser
"""

from django.contrib import admin
from .models import AudioUpload


@admin.register(AudioUpload)
class AudioUploadAdmin(admin.ModelAdmin):
    """
    Customizes how AudioUpload looks in the admin panel.
    This is optional — just admin.site.register(AudioUpload) also works.
    """

    # Columns shown in the list view
    list_display = ['title', 'word_count', 'uploaded_at']

    # Add a search bar that searches these fields
    search_fields = ['title', 'transcription']

    # Add filters in the right sidebar
    list_filter = ['uploaded_at']

    # Make these fields read-only (don't allow editing transcription manually)
    readonly_fields = ['transcription', 'word_count', 'uploaded_at']
