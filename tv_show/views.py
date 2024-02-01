from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic



class Show_Tw_View(generic.ListView):
    model = models.TVShow
    template_name = 'tv_show/tv_shows.html'
    context_object_name = 'tv_shows'
    def get_queryset(self):
        return self.model.objects.all()

# def show_tv_shows(request):
#     if request.method == 'GET':
#         tv_shows = models.TVShow.objects.all()
#         return render(request, template_name='tv_show/tv_shows.html',
#                       context={'tv_shows': tv_shows})

class Show_Tw_Detail_View(generic.DeleteView):
    template_name='tv_show/tv_show_detail.html'
    context_object_name = 'tv_shows_id'
    def get_object(self, **kwargs):
        tv_show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=tv_show_id)

# def show_tv_shows_detail(request, id):
#     if request.method == 'GET':
#         tv_shows_id = get_object_or_404(models.TVShow, id=id)
#         return render(request, template_name='tv_show/tv_show_detail.html',
#                       context={'tv_shows_id': tv_shows_id})

class Show_Tw_Create_View(generic.CreateView):
    template_name = 'tv_show/crud/create_film.html'
    form_class = forms.TVShowForm
    success_url = '/'
    queryset = models.TVShow.objects.all()
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Show_Tw_Create_View, self).form_valid(form=form)
# def create_film_view(request):
#     if request.method == 'POST':
#         form = forms.TVShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен <a href="/">На главную</a>')
#     else:
#         form = forms.TVShowForm()
#         return render(request,
#                   template_name='tv_show/crud/create_film.html',
#                   context={'form': form})


class Delete_Film_View(generic.DeleteView):
    template_name = 'tv_show/crud/confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        tv_show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=tv_show_id)
# def delete_film_view(request, id):
#     tv_shows_id = get_object_or_404(models.TVShow, id=id)
#     tv_shows_id.delete()
#     return HttpResponse('Успешно удален <a href="/">На главную</a> ')


class Edit_Film_View(generic.UpdateView):
    template_name = 'tv_show/crud/edit_film.html'
    form_class = forms.TVShowForm
    success_url = '/'
    queryset = models.TVShow.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Edit_Film_View, self).form_valid(form=form)

    def get_object(self, **kwargs):
        tv_show_id = self.kwargs.get('id')
        return get_object_or_404(models.TVShow, id=tv_show_id)
# def edit_film_view(request, id):
#     tv_shows_id = get_object_or_404(models.TVShow, id=id)
#     if request.method == 'POST':
#         form = forms.TVShowForm(instance=tv_shows_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно изменен <a href="/">На главную</a>')
#     else:
#         form = forms.TVShowForm(instance=tv_shows_id)
#         return render(request,
#                       template_name='tv_show/crud/edit_film.html',
#                       context={'form': form,
#                                'tv_shows_id': tv_shows_id})


class Comment_Fils_View(generic.CreateView):
    template_name = 'tv_show/crud/comment.html'
    form_class = forms.ReviewForm
    success_url = '/'
    queryset = models.Review.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(Comment_Fils_View, self).form_valid(form=form)
        # def comment_film_view(request):
#     if request.method == 'POST':
#         form = forms.ReviewForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Успешно добавлен <a href="/">На главную</a>')
#     else:
#         form = forms.TVShowForm()
#         return render(request,
#                         template_name='tv_show/crud/comment.html',
#                         context={'form': form})

class Search_View(generic.ListView):
    template_name = 'tv_show/tv_shows.html'
    context_object_name = 'tv_shows'
    paginate_by = '5'

    def get_queryset(self):
        return models.TVShow.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context