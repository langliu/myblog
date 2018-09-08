from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from json import loads
from article.models import Article, ArticleTag, Category, ArticleCategory, Tag


@csrf_exempt
def add_article(request):
    if request.method == 'POST':
        post_data = loads(request.body)
        article = Article(title=post_data['title'],
                          content=post_data['content'],
                          create_date=timezone.now(),
                          update_date=timezone.now(),
                          author='allen')
        article.save()
        print(article.id)
        category = Category.objects.filter(name=post_data['category'])
        if not category.exists():
            Category.objects.create(name=post_data['category'])
        ArticleCategory.objects.create(article=article.id, category=category[0].id)
        for item in post_data['tags']:
            tag = Tag.objects.filter(name=item)
            if not tag.exists():
                Tag.objects.create(name=item)
            ArticleTag.objects.create(article=article.id, tag=tag[0].id)
        return JsonResponse({'code': 200})


@csrf_exempt
def get_article_by_id(request):
    if request.method == 'GET':
        article_id = request.GET.get('id')
        print(article_id)
        response_data = model_to_dict(Article.objects.get(pk=article_id))
        category_id = ArticleCategory.objects.get(article=article_id).category
        category = Category.objects.get(pk=category_id).name
        print(category)
        response_data['category'] = category
        return JsonResponse({'code': 200, 'message': '请求成功', 'data': response_data})


@csrf_exempt
def get_article_list(request):
    if request.method == 'GET':
        page = request.GET.get('page')
        page_size = int(request.GET.get('pageSize'))
        response = {}
        article_list = Article.objects.all()
        paginator = Paginator(article_list, page_size)
        response['total'] = paginator.count
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        response['articles'] = loads(serializers.serialize("json", articles))
        print(response)
        return JsonResponse({'code': 200, 'message': '请求成功', 'data': response})
