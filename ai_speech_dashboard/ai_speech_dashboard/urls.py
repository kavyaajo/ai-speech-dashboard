"""
urls.py (Project-level) — The traffic controller of your project.
When a user visits a URL, Django checks this file to figure out
which "view" (Python function) should handle the request.

Think of it like a table of contents:
  URL pattern → Which function handles it
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # /admin/ → Django's built-in admin panel (free dashboard!)
    path('admin/', admin.site.urls),

    # '' (empty) → hand control to speech_app/urls.py
    # include() means: "go look in that other urls.py file"
    path('', include('speech_app.urls')),
]

# During development, this line makes Django serve uploaded files (audio)
# In production, a real web server (Nginx) handles this instead
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
