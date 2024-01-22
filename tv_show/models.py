from django.db import models


class TVShow(models.Model):
    CATRGORY = [
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Детектив', 'Детектив'),
        ('Боевик', 'Боевик'),
        ('Исторические', 'Исторические')
    ]
    name = models.CharField(max_length=50, verbose_name='Укажите название фильма')
    description = models.TextField(verbose_name='Описание фильма')
    image = models.URLField(verbose_name='Вставте фото фильма')
    category = models.CharField(max_length=100, choices=CATRGORY, verbose_name='Выберите котигорию')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}-{self.category}'
