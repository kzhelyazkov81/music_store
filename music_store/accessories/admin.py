from django.contrib import admin

from music_store.accessories.models import Accessory


@admin.register(Accessory)
class AccessoriesAdmin(admin.ModelAdmin):
    pass
