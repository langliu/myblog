from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from django.forms.models import model_to_dict
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
        return JsonResponse({'code': 200, 'message': '请求成功', 'data': response_data})
