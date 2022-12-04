
from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from music_store.accounts.forms import UserEditForm, UserCreationForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(auth_admin.UserAdmin):
    form = UserEditForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", 'address', 'phone_number',)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions",)},),
    )
