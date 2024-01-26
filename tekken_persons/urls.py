from django.urls import path
from . import views


urlpatterns = [
    path('persons_list/', views.persons_list, name='person_list'),
]