from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.views import generic as views
from music_store.common.models import Order

UserModel = get_user_model()


class IndexView(views.TemplateView):
    template_name = 'index.html'


class OrdersTableView(auth_mixins.PermissionRequiredMixin, views.ListView):
    permission_required = 'common.view_order'
    context_object_name = 'articles'
    template_name = 'common/orders.html'
    model = Order
