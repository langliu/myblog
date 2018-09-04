from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200)
    create_date = models.DateField()
    update_date = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=50)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)


class ArticleTag(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.IntegerField()
    tag = models.IntegerField()


class ArticleCategory(models.Model):
    id = models.AutoField(primary_key=True)
    article = models.IntegerField()
    category = models.IntegerField()
