from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.views import generic as views
from django.shortcuts import render, redirect
import sys
from music_store.common.forms import OrderCreateForm
from music_store.common.models import Order
from music_store.guitars.models import Guitar
from music_store.drums.models import DrumSet
from music_store.microphones.models import Microphone
from music_store.keyboards.models import Keyboard
from music_store.accessories.models import Accessory

UserModel = get_user_model()


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


class IndexView(views.TemplateView):
    template_name = 'index.html'


def add_order(request, article_name, pk):
    instance = str_to_class(article_name).objects.get(pk=pk)
    customer = request.user

    if request.method == 'GET':
        form = OrderCreateForm()
    else:
        form = OrderCreateForm(request.POST, instance, customer)
        if form.is_valid():
            order = form.save(commit=False)
            order.article = instance.__class__.__name__
            order.model = instance.model
            order.first_name = customer.first_name
            order.last_name = customer.last_name
            order.address = customer.address
            order.email = customer.email
            order.phone_number = customer.phone_number
            order.save()
            return redirect('index')
    context = {
        'form': form,
        'article_name': article_name,
        'pk': pk,
    }
    return render(
        request,
        template_name='common/order.html',
        context=context,
    )


class OrdersTableView(auth_mixins.PermissionRequiredMixin, views.ListView):
    permission_required = 'common.view_order'
    context_object_name = 'articles'
    template_name = 'common/orders.html'
    model = Order
