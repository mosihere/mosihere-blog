from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Article




def article_index(request):
    articles = Article.objects.all().order_by('-pub_date')
    context = {'articles': articles}
    return render(request, 'blog/article_index.html', context)


def article_detail(request, slug):
    this_article = Article.objects.get(slug=slug)
    context = {'this_article': this_article, 'slug':slug}
    return render(request, 'blog/article_detail.html', context)