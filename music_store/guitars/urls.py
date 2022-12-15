from django.urls import path

from music_store.guitars.views import \
    GuitarEditView, GuitarDetailsView, GuitarDeleteView, GuitarsCatalogView, GuitarCreateView, add_order

urlpatterns = [
    path('catalog/', GuitarsCatalogView.as_view(), name='guitars-catalog'),
    path('create/', GuitarCreateView.as_view(), name='guitar-create'),
    path('edit/<int:pk>/', GuitarEditView.as_view(), name='guitar-edit'),
    path('details/<int:pk>/', GuitarDetailsView.as_view(), name='guitar-details'),
    path('delete/<int:pk>/', GuitarDeleteView.as_view(), name='guitar-delete'),
    path('order/<int:pk>', add_order, name='guitar-order'),

]
