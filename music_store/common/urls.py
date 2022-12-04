
from django.urls import path

from music_store.common.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
)
