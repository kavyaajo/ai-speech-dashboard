# AI Speech Transcription Dashboard

A Django-based web application that allows users to upload audio files and get text transcriptions.

## Features
- Upload audio files (.wav, .mp3)
- Automatic speech-to-text conversion
- Handles long audio using chunk processing
- Dashboard showing all uploads
- View detailed transcription
- Delete recordings

## Tech Stack
- Django (Backend)
- HTML, CSS (Frontend)
- SpeechRecognition (Python)
- Google Speech API

## How it Works
Audio is split into chunks and processed to avoid API limits, ensuring full transcription for long audio files.
