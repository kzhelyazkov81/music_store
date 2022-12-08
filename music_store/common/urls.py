
from django.urls import path

from music_store.common.views import IndexView, add_order, OrdersTableView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('order/<str:article_name>/<int:pk>/<int:user_id>/', add_order, name='order'),
    path('orders/', OrdersTableView.as_view(), name='orders'),
)
