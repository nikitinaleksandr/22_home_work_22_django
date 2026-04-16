from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Содержимое', blank=True, null=True)
    image = models.ImageField(upload_to='images', verbose_name='Превью', blank=True, null=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров", help_text="Укажите количество просмотров" )


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ['-create_at']
