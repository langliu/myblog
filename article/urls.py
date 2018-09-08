from django.urls import path
from . import views

urlpatterns = [
    path('addArticle', views.add_article, name='add_article'),
    path('getArticleDetail', views.get_article_by_id, name='get_article_detail'),
    path('getArticleList', views.get_article_list, name='get_article_list')
]
