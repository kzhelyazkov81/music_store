from django.contrib import admin

from music_store.guitars.models import Guitar


@admin.register(Guitar)
class GuitarAdmin(admin.ModelAdmin):
    pass
