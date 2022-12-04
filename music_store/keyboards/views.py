from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins


from music_store.keyboards.forms import KeyboardCreateForm, KeyboardEditForm
from music_store.keyboards.models import Keyboard


class KeyboardsCatalogView(views.ListView):
    context_object_name = 'articles'
    template_name = 'articles/keyboards/keyboards.html'
    model = Keyboard


class KeyboardCreateView(auth_mixins.PermissionRequiredMixin, views.CreateView):
    permission_required = 'keyboards.add_keyboard'
    template_name = 'articles/keyboards/keyboard-create.html'
    model = Keyboard
    form_class = KeyboardCreateForm
    success_url = reverse_lazy('keyboards-catalog')


class KeyboardDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    context_object_name = 'articles'
    template_name = 'articles/keyboards/keyboard-details.html'
    model = Keyboard


class KeyboardEditView(auth_mixins.PermissionRequiredMixin, views.UpdateView):
    permission_required = 'keyboards.change_keyboard'
    template_name = 'articles/keyboards/keyboard-edit.html'
    model = Keyboard
    form_class = KeyboardEditForm

    def get_success_url(self):
        return reverse_lazy('keyboard-details', kwargs={
            'pk': self.object.pk,
        })


class KeyboardDeleteView(auth_mixins.PermissionRequiredMixin, views.DeleteView):
    permission_required = 'keyboards.delete_keyboard'
    template_name = 'articles/keyboards/keyboard-delete.html'
    model = Keyboard
    success_url = reverse_lazy('keyboards-catalog')
