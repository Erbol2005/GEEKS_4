from django.urls import path
from . import views


urlpatterns = [
    path('', views.Show_Tw_View.as_view(), name='show_tv_show'),
    path('show_tv_shows/<int:id>/', views.Show_Tw_Detail_View.as_view(), name='show_tv_show_detail'),
    path('show_tv_shows/<int:id>/delete/', views.Delete_Film_View.as_view(), name='delete_film'),
    path('show_tv_shows/<int:id>/update/', views.Edit_Film_View.as_view(), name='edit_film'),
    path('create_film/', views.Show_Tw_Create_View.as_view(), name='create_film'),
    path('create_review/', views.Comment_Fils_View.as_view(), name='create_review'),
    path('search/', views.Search_View.as_view(), name='search'),
]