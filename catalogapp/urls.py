from django.urls import path

from catalogapp.views import home, contacts

urlpatterns = [
    path('', home),
    path('contacts/', contacts)
]
