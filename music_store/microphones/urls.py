from django.urls import path

from music_store.microphones.views import MicrophonesCatalogView, MicrophoneCreateView, \
    MicrophoneEditView, MicrophoneDetailsView, MicrophoneDeleteView

urlpatterns = [
    path('catalog/', MicrophonesCatalogView.as_view(), name='microphones-catalog'),
    path('create/', MicrophoneCreateView.as_view(), name='microphone-create'),
    path('edit/<int:pk>', MicrophoneEditView.as_view(), name='microphone-edit'),
    path('details/<int:pk>', MicrophoneDetailsView.as_view(), name='microphone-details'),
    path('delete/<int:pk>', MicrophoneDeleteView.as_view(), name='microphone-delete'),
]
