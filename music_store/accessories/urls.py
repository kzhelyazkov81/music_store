from django.urls import path

from music_store.accessories.views import AccessoriesCatalogView, AccessoryCreateView, AccessoryEditView, \
    AccessoryDetailsView, AccessoryDeleteView, add_order

urlpatterns = [
    path('catalog/', AccessoriesCatalogView.as_view(), name='accessories-catalog'),
    path('create/', AccessoryCreateView.as_view(), name='accessory-create'),
    path('edit/<int:pk>', AccessoryEditView.as_view(), name='accessory-edit'),
    path('details/<int:pk>', AccessoryDetailsView.as_view(), name='accessory-details'),
    path('delete/<int:pk>', AccessoryDeleteView.as_view(), name='accessory-delete'),
    path('order/<int:pk>', add_order, name='accessory-order'),
]
