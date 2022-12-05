from django import forms

from music_store.accessories.models import Accessory


class AccessoryCreateForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = '__all__'


class AccessoryEditForm(AccessoryCreateForm):
    class Meta:
        model = Accessory
        exclude = ('type', 'model')
