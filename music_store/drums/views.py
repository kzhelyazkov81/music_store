from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from music_store.common.forms import OrderCreateForm
from music_store.drums.forms import DrumSetCreateForm, DrumSetEditForm
from music_store.drums.models import DrumSet


class DrumSetsCatalogView(views.ListView):
    context_object_name = 'articles'
    template_name = 'articles/drums/drums.html'
    model = DrumSet


class DrumSetCreateView(auth_mixins.PermissionRequiredMixin, views.CreateView):
    permission_required = 'drums.add_drumset'
    template_name = 'articles/drums/drums-create.html'
    model = DrumSet
    form_class = DrumSetCreateForm
    success_url = reverse_lazy('drums-catalog')


class DrumSetDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    context_object_name = 'articles'
    template_name = 'articles/drums/drums-details.html'
    model = DrumSet


class DrumSetEditView(auth_mixins.PermissionRequiredMixin, views.UpdateView):
    permission_required = 'drums.change_drumset'
    template_name = 'articles/drums/drums-edit.html'
    model = DrumSet
    form_class = DrumSetEditForm

    def get_success_url(self):
        return reverse_lazy('drums-details', kwargs={
            'pk': self.object.pk,
        })


class DrumSetDeleteView(auth_mixins.PermissionRequiredMixin, views.DeleteView):
    permission_required = 'drums.delete_drumset'
    template_name = 'articles/drums/drums-delete.html'
    model = DrumSet
    success_url = reverse_lazy('guitars-catalog')


def add_order(request, pk):
    instance = DrumSet.objects.get(pk=pk)

    if request.method == 'GET':
        form = OrderCreateForm()
    else:
        form = OrderCreateForm(request.POST, instance)
        if form.is_valid():
            order = form.save(commit=False)
            order.article = 'Drum Set'
            order.model = instance.model
            order.first_name = request.user.first_name
            order.last_name = request.user.last_name
            order.address = request.user.address
            order.email = request.user.email
            order.phone_number = request.user.phone_number
            order.save()
            return redirect('index')
    context = {
        'form': form,
        'pk': pk,
    }
    return render(
        request,
        template_name='articles/drums/drums-order.html',
        context=context,
    )
