from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins


from music_store.accessories.forms import AccessoryCreateForm, AccessoryEditForm
from music_store.accessories.models import Accessory


class AccessoriesCatalogView(views.ListView):
    context_object_name = 'articles'
    template_name = 'articles/accessories/accessories.html'
    model = Accessory


class AccessoryCreateView(auth_mixins.PermissionRequiredMixin, views.CreateView):
    permission_required = 'accessories.add_accessory'
    template_name = 'articles/accessories/accessory-create.html'
    model = Accessory
    form_class = AccessoryCreateForm
    success_url = reverse_lazy('accessories-catalog')


class AccessoryDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    context_object_name = 'articles'
    template_name = 'articles/accessories/accessory-details.html'
    model = Accessory


class AccessoryEditView(auth_mixins.PermissionRequiredMixin, views.UpdateView):
    permission_required = 'accessories.change_accessory'
    template_name = 'articles/accessories/accessory-edit.html'
    model = Accessory
    form_class = AccessoryEditForm

    def get_success_url(self):
        return reverse_lazy('accessory-details', kwargs={
            'pk': self.object.pk,
        })


class AccessoryDeleteView(auth_mixins.PermissionRequiredMixin, views.DeleteView):
    permission_required = 'accessories.delete_accessory'
    template_name = 'articles/accessories/accessory-delete.html'
    model = Accessory
    success_url = reverse_lazy('accessories-catalog')
