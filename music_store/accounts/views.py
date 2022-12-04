from django.contrib.auth import views as auth_views, get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views
from music_store.accounts.forms import UserCreationForm
UserModel = get_user_model()


class SignUpView(views.CreateView):
    template_name = 'accounts/account-create.html'
    form_class = UserCreationForm

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result

    success_url = reverse_lazy('index')


class SignInView(auth_views.LoginView):
    template_name = 'accounts/account-login.html'
    next_page = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserEditView(views.UpdateView):
    template_name = 'accounts/account-edit.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'email', 'address', 'phone_number')

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={
            'pk': self.request.user.pk,
        })


class UserDetailsView(views.DetailView):
    template_name = 'accounts/account-profile.html'
    model = UserModel


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/account-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')
