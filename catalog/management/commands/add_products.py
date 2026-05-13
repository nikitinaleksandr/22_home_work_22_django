from itertools import product

from django.core.management.base import BaseCommand
from catalog.models import Product,Category

class Command(BaseCommand):
    help = 'Add product to the data base'

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        category, _ = Category.objects.get_or_create(name='фрукты', description = 'цитрусовые')
        products_to_add  = [
            {'name': 'апельсин', 'price': '100', 'category': category},
            {'name': 'грейпфрут', 'price': '120', 'category': category},
            {'name': 'лимон', 'price': '130', 'category': category},
        ]

        for product_data in products_to_add :
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Succsessfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.name}'))
