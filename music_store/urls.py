from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('music_store.accounts.urls')),
    path('', include('music_store.common.urls')),
    path('guitars/', include('music_store.guitars.urls')),
    path('drums/', include('music_store.drums.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
