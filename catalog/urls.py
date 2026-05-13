

from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import HomeView
from catalog.views import ContactsView, ProductListView, ProductDetailView, ExampleView, IndexView
from . import views


catalog_name = CatalogConfig.name
app_name = 'catalog'
urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('index/', views.IndexView.as_view(), name='index'),

    path('product_list/', ProductListView.as_view(), name='product_list'),

    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    ]
