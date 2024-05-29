from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ContactsTemplateView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('catalog_product/', ProductListView.as_view(), name='catalog'),
    path('info_product/<int:pk>', ProductDetailView.as_view(), name='info_product')
]
