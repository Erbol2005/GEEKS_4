# Generated by Django 3.2.5 on 2024-01-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default=1, max_length=300, verbose_name='Коментарии'),
            preserve_default=False,
        ),
    ]
