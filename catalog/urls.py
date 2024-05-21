from django.urls import path

from catalog.views import home, contacts, catalog, info_product

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('catalog_product/', catalog, name='catalog'),
    path('info_product/<int:pk>', info_product, name='info_product')
]
