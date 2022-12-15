
from django.urls import path

from music_store.common.views import IndexView, OrdersTableView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('orders/', OrdersTableView.as_view(), name='orders'),
)
