from django.contrib import admin
from django.db import models
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pub_date']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)
