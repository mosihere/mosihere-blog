from django.contrib import admin
from django.db import models
from .models import Article, Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)




class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Comment, CommentAdmin)