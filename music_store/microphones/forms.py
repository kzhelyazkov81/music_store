from django import forms

from music_store.microphones.models import Microphone


class MicrophoneCreateForm(forms.ModelForm):
    class Meta:
        model = Microphone
        fields = '__all__'


class MicrophoneEditForm(MicrophoneCreateForm):
    class Meta:
        model = Microphone
        exclude = ('model', 'type')
