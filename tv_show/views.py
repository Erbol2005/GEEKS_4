from django.shortcuts import render, get_object_or_404
from . import models

def show_tv_shows(request):
    if request.method == 'GET':
        tv_shows = models.TVShow.objects.all()
        return render(request, template_name='tv_show/tv_shows.html',
                      context={'tv_shows': tv_shows})


def show_tv_shows_detail(request, id):
    if request.method == 'GET':
        tv_shows_id = get_object_or_404(models.TVShow, id=id)
        return render(request, template_name='tv_show/tv_show_detail.html',
                      context={'tv_shows_id': tv_shows_id})