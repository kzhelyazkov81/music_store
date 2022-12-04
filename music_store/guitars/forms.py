from django import forms

from music_store.guitars.models import Guitar


class GuitarCreateForm(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = '__all__'


class GuitarEditForm(GuitarCreateForm):
    class Meta:
        model = Guitar
        exclude = ('model', 'type')
