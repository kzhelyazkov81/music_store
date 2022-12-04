from django.contrib import admin

from music_store.keyboards.models import Keyboard


@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    pass
