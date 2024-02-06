from django.shortcuts import render
from django import forms
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import FormView
from . import models, parser_rezka

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka.ag', 'rezka.ag'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)


class ParserView(FormView):
    template_name = 'parser_form.html'
    form_class = ParserForm

    def form_valid(self, form):
        media_type = form.cleaned_data['media_type']
        if media_type == 'rezka.ag':
            film_parser_rezka = parser_rezka.parser_rezka()
            for i in film_parser_rezka:
                models.RezkaFilms.objects.create(**i)
            return redirect(reverse('parsed_results'))
        return HttpResponse('Данные успешно взяты.......')


class ParsedResultsView(FormView):
    template_name = 'parsed_results.html'

    def get(self, request, *args, **kwargs):
        films = models.RezkaFilms.objects.all()
        return render(request, self.template_name, {'films': films})
