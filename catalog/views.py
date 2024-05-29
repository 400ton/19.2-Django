from catalog.models import Product
from django.views.generic import ListView, DetailView, TemplateView
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


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/catalog_product.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/info_product.html'
