from tkinter.constants import CASCADE

from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание товара",
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    image = models.ImageField(upload_to='images', verbose_name='Изображение', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=150, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена за покупку")
    create_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['-create_at']