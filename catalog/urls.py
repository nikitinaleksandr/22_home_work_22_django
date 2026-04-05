

from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home
from catalog.views import contacts
from . import views


catalog_name = CatalogConfig.name
app_name = 'catalog'
urlpatterns = [

    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('index/', views.index, name='index'),

    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),

    ]
