from itertools import product
from wsgiref.util import request_uri
from catalog.models import Product

from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, "home.html")

# Create your views here.

def contacts(request):
    return render(request, "contacts.html")


def example_view(request):
    return render(request, 'catalog/example.html')


def index(request):
    product =  Product.objects.get(id=5)
    context = {
        'product_name': product.name,
        'product_price':  product.price,
    }
    return render(request, 'catalog/index.html', context=context)


# def product_detail(request):
#     product =  Product.objects.get(id=5)
#     context = {
#         'product': product,
#     }
#     return render(request, 'catalog/product_detail.html', context=context)
def product_detail(request, product_id):  # ← ДОБАВЛЕН параметр product_id
    product = get_object_or_404(Product, id=product_id)  # ← ПОЛУЧАЕТ товар по ID из URL
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context=context)

def product_list(request):
    product = Product.objects.all()
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_list.html', context=context)

