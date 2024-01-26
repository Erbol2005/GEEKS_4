# Generated by Django 3.2.5 on 2024-01-19 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Укажите имя персонажа')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Укажите почту')),
                ('age', models.PositiveIntegerField(default=15, verbose_name='Укажите возраст персонажа')),
                ('image', models.URLField(verbose_name='Вставте фото персонажа')),
                ('capabilitis', models.CharField(max_length=100, verbose_name='Укажите способности персонажа')),
                ('stort', models.CharField(choices=[('Карате', 'Карате'), ('Кунг-фу', 'Кунг-фу'), ('Бокс', 'Бокс'), ('Рестлинг', 'Рестлинг'), ('Ниндзютсу', 'Ниндзютсу')], max_length=100, verbose_name='Выберите стиль персонажа')),
                ('video_url', models.URLField(verbose_name='Вставте видео ссылку')),
            ],
        ),
    ]