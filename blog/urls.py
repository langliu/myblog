from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('article/<int:article_id>/', views.article_page,
         name='article_page'),
    path('edit_page/<int:article_id>/', views.edit_page, name='edit_page'),
    path('edit_action/', views.edit_action, name='edit_action')
]
app_name = 'blog'
