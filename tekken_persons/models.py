from django.db import models

class PersonGame(models.Model):
    SPORT = (
        ('Карате', 'Карате'),
        ('Кунг-фу', 'Кунг-фу'),
        ('Бокс', 'Бокс'),
        ('Рестлинг', 'Рестлинг'),
        ('Ниндзютсу', 'Ниндзютсу'),
    )
    name = models.CharField(max_length=30, verbose_name='Укажите имя персонажа', null=True)
    email = models.EmailField(verbose_name='Укажите почту', blank=True)
    age = models.PositiveIntegerField(default=15, verbose_name='Укажите возраст персонажа')
    image = models.URLField(verbose_name='Вставте фото персонажа')
    capabilitis = models.CharField(max_length=100, verbose_name='Укажите способности персонажа')
    sport = models.CharField(max_length=100, choices=SPORT, verbose_name='Выберите стиль персонажа', null=True)
    video_url = models.URLField(verbose_name='Вставте видео ссылку')

    def __str__(self):
        return f'{self.name}-{self.sport}'

    class Meta:
        verbose_name = 'Персонажа'
