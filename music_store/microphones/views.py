from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from music_store.common.forms import OrderCreateForm
from music_store.microphones.forms import MicrophoneCreateForm, MicrophoneEditForm
from music_store.microphones.models import Microphone
from django.contrib.auth.decorators import login_required


class MicrophonesCatalogView(views.ListView):
    context_object_name = 'articles'
    template_name = 'articles/microphones/microphones.html'
    model = Microphone


class MicrophoneCreateView(auth_mixins.PermissionRequiredMixin, views.CreateView):
    permission_required = 'microphones.add_microphone'
    template_name = 'articles/microphones/microphone-create.html'
    model = Microphone
    form_class = MicrophoneCreateForm
    success_url = reverse_lazy('microphones-catalog')


class MicrophoneDetailsView(auth_mixins.LoginRequiredMixin, views.DetailView):
    context_object_name = 'articles'
    template_name = 'articles/microphones/microphone-details.html'
    model = Microphone


class MicrophoneEditView(auth_mixins.PermissionRequiredMixin, views.UpdateView):
    permission_required = 'microphones.change_microphone'
    template_name = 'articles/microphones/microphone-edit.html'
    model = Microphone
    form_class = MicrophoneEditForm

    def get_success_url(self):
        return reverse_lazy('microphone-details', kwargs={
            'pk': self.object.pk,
        })


class MicrophoneDeleteView(auth_mixins.PermissionRequiredMixin, views.DeleteView):
    permission_required = 'microphones.delete_microphone'
    template_name = 'articles/microphones/microphone-delete.html'
    model = Microphone
    success_url = reverse_lazy('microphones-catalog')


@login_required
def add_order(request, pk):
    instance = Microphone.objects.get(pk=pk)

    if request.method == 'GET':
        form = OrderCreateForm()
    else:
        form = OrderCreateForm(request.POST, instance)
        if form.is_valid():
            order = form.save(commit=False)
            order.article = 'Microphone'
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
        template_name='articles/microphones/microphone-order.html',
        context=context,
    )
