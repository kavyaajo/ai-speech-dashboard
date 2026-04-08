"""
0001_initial.py — The first migration for speech_app.

Django auto-generates this when you run:
  python manage.py makemigrations

You should NEVER edit migration files manually.
They are Django's way of tracking database changes over time —
like version control for your database schema.

This migration creates the speech_app_audioupload table in db.sqlite3.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='AudioUpload',
            fields=[
                # Django auto-creates 'id' as the primary key
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text="A label for this recording", max_length=200)),
                ('audio_file', models.FileField(help_text="The uploaded .wav or .mp3 file", upload_to='uploads/')),
                ('transcription', models.TextField(blank=True, help_text="The speech-to-text result")),
                ('word_count', models.IntegerField(default=0, help_text="Number of words in the transcription")),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, help_text="When this file was uploaded")),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
    ]
