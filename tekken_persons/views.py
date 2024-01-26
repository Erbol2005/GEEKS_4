from django.shortcuts import render, get_object_or_404
from . import models


def persons_list(request):
    if request.method == 'GET':
        persons = models.PersonGame.objects.all()
        return render(request, template_name='tekken_game/persons_list.html',
<<<<<<< HEAD
                      context={'persons': persons})
=======
                      context={'persons': persons} )
>>>>>>> 071e9cfa7983c41df8fa0223e0105b965cce1eba


def persons_detail(reqvest, id):
    if reqvest.method == 'GET':
        person_id = get_object_or_404(models.PersonGame, id=id)
        return render(reqvest, template_name='tekken_game/persons_detail.html',
                      context={'person_id': person_id}
                      )