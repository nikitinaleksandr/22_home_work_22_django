from tkinter.font import names

from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home
from catalog.views import contacts

catalog_name = CatalogConfig.name
app_name = 'catalog'
urlpatterns = [

    path('', home, name='home'),
    path('contacts/', contacts, name='contacts')
    ]