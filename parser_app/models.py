from django.db import models

class RezkaFilms(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
