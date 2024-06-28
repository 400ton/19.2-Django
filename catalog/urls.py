from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (HomeTemplateView, ContactsTemplateView, ProductListView, ProductDetailView,
                           ProductDeleteView, ProductCreateView, ProductUpdateView, CategoryListView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('list/', ProductListView.as_view(), name='list'),
    path('detail/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='detail'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>', ProductUpdateView.as_view(), name='update'),
    path('category/', CategoryListView.as_view(), name='list_category')
]
