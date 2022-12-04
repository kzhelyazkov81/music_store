from django.urls import path

from music_store.drums.views import DrumSetsCatalogView, DrumSetCreateView,\
    DrumSetEditView, DrumSetDetailsView, DrumSetDeleteView

urlpatterns = [
    path('catalog/', DrumSetsCatalogView.as_view(), name='drums-catalog'),
    path('create/', DrumSetCreateView.as_view(), name='drums-create'),
    path('edit/<int:pk>', DrumSetEditView.as_view(), name='drums-edit'),
    path('details/<int:pk>', DrumSetDetailsView.as_view(), name='drums-details'),
    path('delete/<int:pk>', DrumSetDeleteView.as_view(), name='drums-delete'),
]
