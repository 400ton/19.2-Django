from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (HomeTemplateView, ContactsTemplateView, ProductListView, ProductDetailView,
                           ProductDeleteView, ProductCreateView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('list/', ProductListView.as_view(), name='list'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create')
]
