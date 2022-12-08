from django.contrib import admin

from music_store.common.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
