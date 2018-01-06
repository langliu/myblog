from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'public_time')
    list_filter = ('public_time',)


# Register your models here.
admin.site.register(Article, ArticleAdmin)
