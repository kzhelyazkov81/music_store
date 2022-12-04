from django import forms

from music_store.keyboards.models import Keyboard


class KeyboardCreateForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = '__all__'


class KeyboardEditForm(KeyboardCreateForm):
    class Meta:
        model = Keyboard
        exclude = ('model',)
