from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название киги')
    description = models.TextField(verbose_name='Описание книги')
    image = models.ImageField(upload_to='')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена книги')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title