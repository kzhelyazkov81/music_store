from django.urls import path, include
from django.contrib import admin

from music_store.accounts.views import SignUpView, SignInView, \
    UserEditView, UserDetailsView, SignOutView, UserDeleteView

urlpatterns = (
    path('create/', SignUpView.as_view(), name='create'),
    path('login/', SignInView.as_view(), name='login'),
    path('edit/<int:pk>/', UserEditView.as_view(), name='edit'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='profile'),
        path('edit/', UserEditView.as_view(), name='edit profile'),
        path('delete/', UserDeleteView.as_view(), name='delete profile'),
    ])),
)
