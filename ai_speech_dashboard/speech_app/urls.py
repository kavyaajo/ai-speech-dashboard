"""
urls.py (App-level) — URL patterns specific to speech_app.

This file is included by the project-level urls.py.
Each path() entry maps a URL pattern to a view function.

path() takes:
  1. URL pattern (string)   — what the user types in the browser
  2. View function          — what Python function handles it
  3. name=''                — a nickname to reference this URL in templates

URL Pattern Syntax:
  ''           → matches exactly /  (homepage)
  'upload/'    → matches /upload/
  '<int:pk>/'  → matches /detail/1/ or /detail/42/ — captures the number as 'pk'

The name= parameter is important!
In templates, instead of hardcoding '/upload/', you write:
  {% url 'upload_audio' %}
This means if you ever change the URL, templates update automatically.
"""

from django.urls import path
from . import views  # Import all view functions from this app's views.py

urlpatterns = [
    # / → dashboard (homepage showing all uploads)
    path('', views.dashboard, name='dashboard'),

    # /upload/ → upload form
    path('upload/', views.upload_audio, name='upload_audio'),

    # /detail/1/ → detail view for upload with pk=1
    # <int:pk> captures the integer from the URL and passes it to the view
    path('detail/<int:pk>/', views.detail, name='detail'),

    # /delete/1/ → delete upload with pk=1
    path('delete/<int:pk>/', views.delete_upload, name='delete_upload'),

    path('delete/<int:id>/', views.delete_upload, name='delete_audio'),
]

