# Generated by Django 3.2.5 on 2024-01-22 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='films',
            new_name='TVShow',
        ),
    ]
