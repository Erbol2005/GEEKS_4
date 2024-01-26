from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
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


def create_film_view(request):
    if request.method == 'POST':
        form = forms.TVShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавлен <a href="/">На главную</a>')
    else:
        form = forms.TVShowForm()
        return render(request,
                  template_name='tv_show/crud/create_film.html',
                  context={'form': form})

def delete_film_view(request, id):
    tv_shows_id = get_object_or_404(models.TVShow, id=id)
    tv_shows_id.delete()
    return HttpResponse('Успешно удален <a href="/">На главную</a> ')

def edit_film_view(request, id):
    tv_shows_id = get_object_or_404(models.TVShow, id=id)
    if request.method == 'POST':
        form = forms.TVShowForm(instance=tv_shows_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно изменен <a href="/">На главную</a>')
    else:
        form = forms.TVShowForm(instance=tv_shows_id)
        return render(request,
                      template_name='tv_show/crud/edit_film.html',
                      context={'form': form,
                               'tv_shows_id': tv_shows_id})

def comment_film_view(request, id):
    review = get_object_or_404(models.Review, id=id)

    if request.method == 'POST':
        form = forms.TVShowForm(request.POST)
        if form.is_valid():
            review_instance = form.save(commit=False)
            review_instance.tv_show = review.tv_show
            review_instance.save()
            return HttpResponse('Успешно добавлен <a href="/">На главную</a>')
    else:
        form = forms.TVShowForm()

    return render(request,
                  template_name='tv_show/crud/comment.html',
                  context={'form': form, 'review': review})

