from django import forms

from music_store.common.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('quantity',)
