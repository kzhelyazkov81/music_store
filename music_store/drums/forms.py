from django import forms

from music_store.drums.models import DrumSet


class DrumSetCreateForm(forms.ModelForm):
    class Meta:
        model = DrumSet
        fields = '__all__'


class DrumSetEditForm(DrumSetCreateForm):
    class Meta:
        model = DrumSet
        exclude = ('model',)
