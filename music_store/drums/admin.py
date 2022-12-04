from django.contrib import admin

from music_store.drums.models import DrumSet


@admin.register(DrumSet)
class DrumSetAdmin(admin.ModelAdmin):
    pass
