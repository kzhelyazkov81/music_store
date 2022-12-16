from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from music_store.common.forms import OrderCreateForm
from music_store.keyboards.forms import KeyboardCreateForm, KeyboardEditForm
from music_store.keyboards.models import Keyboard
from django.contrib.auth.decorators import login_required


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


@login_required
def add_order(request, pk):
    instance = Keyboard.objects.get(pk=pk)

    if request.method == 'GET':
        form = OrderCreateForm()
    else:
        form = OrderCreateForm(request.POST, instance)
        if form.is_valid():
            order = form.save(commit=False)
            order.article = 'Keyboard'
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
        template_name='articles/keyboards/keyboard-order.html',
        context=context,
    )
