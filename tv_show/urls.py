from django.urls import path
from . import views


urlpatterns = [
    path('show_tv_shows/', views.show_tv_shows, name='show_tv_show'),
    path('show_tv_shows/<int:id>/', views.show_tv_shows_detail, name='show_tv_show_detail'),

]