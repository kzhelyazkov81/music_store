from django.urls import path

from music_store.guitars.views import \
    GuitarEditView, GuitarDetailsView, GuitarDeleteView, GuitarsCatalogView, GuitarCreateView

urlpatterns = [
    path('catalog/', GuitarsCatalogView.as_view(), name='guitars-catalog'),
    path('create/', GuitarCreateView.as_view(), name='guitar-create'),
    path('edit/<int:pk>', GuitarEditView.as_view(), name='guitar-edit'),
    path('details/<int:pk>', GuitarDetailsView.as_view(), name='guitar-details'),
    path('delete/<int:pk>', GuitarDeleteView.as_view(), name='guitar-delete'),
]

