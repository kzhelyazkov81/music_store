from django.contrib import admin

from music_store.microphones.models import Microphone


@admin.register(Microphone)
class MicrophoneAdmin(admin.ModelAdmin):
    pass
