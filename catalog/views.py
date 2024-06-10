from catalog.forms import ProductForm
from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
import datetime


class HomeTemplateView(TemplateView):
    template_name = "catalog/home.html"


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open('feedback.txt', 'a') as file:
            file.write(f'{timestamp}, {phone}, {name}: {message}\n')
        return super().get(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:list')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить продукт'
        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:list')
