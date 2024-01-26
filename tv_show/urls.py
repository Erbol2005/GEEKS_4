from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_tv_shows, name='show_tv_show'),
    path('show_tv_shows/<int:id>/', views.show_tv_shows_detail, name='show_tv_show_detail'),
    path('show_tv_shows/<int:id>/delete/', views.delete_film_view, name='delete_film'),
    path('show_tv_shows/<int:id>/update/', views.edit_film_view, name='edit_film'),
    path('show_tv_shows/<int:id>/review/', views.comment_film_view, name='comment_film'),
    path('create_film/', views.create_film_view, name='create_film'),

    path('show_tv_shows/', views.show_tv_shows, name='show_tv_show'),
    path('show_tv_shows/<int:id>/', views.show_tv_shows_detail, name='show_tv_show_detail'),

]