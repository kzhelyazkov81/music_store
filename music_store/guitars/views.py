from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model


from music_store.guitars.forms import GuitarCreateForm, GuitarEditForm
from music_store.guitars.models import Guitar


class GuitarsCatalogView(views.ListView):
    context_object_name = 'articles'
    template_name = 'articles/guitars/guitars.html'
    model = Guitar


class GuitarCreateView(auth_mixins.PermissionRequiredMixin, views.CreateView):
    permission_required = 'guitars.add_guitar'
    template_name = 'articles/guitars/guitar-create.html'
    model = Guitar
    form_class = GuitarCreateForm
    success_url = reverse_lazy('guitars-catalog')


class GuitarDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    context_object_name = 'articles'
    template_name = 'articles/guitars/guitar-details.html'
    model = Guitar


class GuitarEditView(auth_mixins.PermissionRequiredMixin, views.UpdateView):
    permission_required = 'guitars.change_guitar'
    template_name = 'articles/guitars/guitar-edit.html'
    model = Guitar
    form_class = GuitarEditForm

    def get_success_url(self):
        return reverse_lazy('guitar-details', kwargs={
            'pk': self.object.pk,
        })


class GuitarDeleteView(auth_mixins.PermissionRequiredMixin, views.DeleteView):
    permission_required = 'guitars.delete_guitar'
    template_name = 'articles/guitars/guitar-delete.html'
    model = Guitar
    success_url = reverse_lazy('guitars-catalog')

