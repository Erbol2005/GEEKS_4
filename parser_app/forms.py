from django import forms
from . import models, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        'rezka.ag', 'rezka.ag'
    ),
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)


    class Meta:
        fields = ['media_type',]


        def parser_data(self):
            if self.data['media_type'] == 'rezka.ag':
                film_parser_rezka = parser_rezka.parser_rezka()
                for i in film_parser_rezka:
                    models.RezkaFilms.objects.create(**i)