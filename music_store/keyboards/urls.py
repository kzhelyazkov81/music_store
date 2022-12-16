from django.urls import path

from music_store.keyboards.views import KeyboardsCatalogView, KeyboardCreateView, KeyboardEditView, KeyboardDeleteView, \
    KeyboardDetailsView, add_order

urlpatterns = [
    path('catalog/', KeyboardsCatalogView.as_view(), name='keyboards-catalog'),
    path('create/', KeyboardCreateView.as_view(), name='keyboard-create'),
    path('edit/<int:pk>/', KeyboardEditView.as_view(), name='keyboard-edit'),
    path('details/<int:pk>/', KeyboardDetailsView.as_view(), name='keyboard-details'),
    path('delete/<int:pk>/', KeyboardDeleteView.as_view(), name='keyboard-delete'),
    path('order/<int:pk>/', add_order, name='keyboard-order'),
]
