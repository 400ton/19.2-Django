from django.shortcuts import render, get_object_or_404
from catalog.models import Product
import datetime


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        telephone = request.POST.get('phone')
        message = request.POST.get('message')
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        with open('feedback.txt', 'a') as file:
            file.write(f'{timestamp}, {name},{telephone}: {message}\n')

    return render(request, 'catalog/contacts.html')
def catalog(request):
    product_list = Product.objects.all()
    context = {'objects_list': product_list}
    return render(request, 'catalog/catalog_product.html', context)


def info_product(request, pk):
    context = {'object': get_object_or_404(Product, pk=pk)}
    return render(request, "catalog/info_product.html", context)