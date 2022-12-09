from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
from .forms import PageForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator



class ProductList(ListView):

    model = Product


class ProductDetail(DetailView):

    model = Product


@method_decorator(staff_member_required, name='dispatch')
class ProductCreate(CreateView):

    model = Product
    form_class = PageForm
    success_url = reverse_lazy('productos:productos')


@method_decorator(staff_member_required, name='dispatch')
class ProductUpdate(UpdateView):
    model = Product
    form_class = PageForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('productos:productos')

    def get_success_url(self):
        return reverse_lazy('productos:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('productos:productos')



