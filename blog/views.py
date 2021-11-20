from django.shortcuts import get_object_or_404, render

from blog.forms import CommentForm
from .models import Article, Comment




def article_index(request):
    articles = Article.objects.all().order_by('-pub_date')
    context = {'articles': articles}
    return render(request, 'blog/article_index.html', context)


def article_detail(request, slug):
    this_article = get_object_or_404(Article, slug=slug)
    comments = this_article.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = this_article
            new_comment.save()
    
    else:
        comment_form = CommentForm()

    return render(request, 'blog/article_detail.html', context={'this_article': this_article, 'comments':comments, 'new_comment':new_comment, 'comment_form':comment_form})