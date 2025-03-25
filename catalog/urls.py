from tkinter.font import names

from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home
catalog_name = CatalogConfig.name
app_name = 'catalog'
urlpatterns = [

    path('', home, name='home')
]