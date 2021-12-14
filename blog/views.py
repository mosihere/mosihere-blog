from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from blog.forms import CommentForm
from django.http import HttpResponseRedirect
from .models import Article


def article_like(request, slug):
    post = get_object_or_404(Article, id=request.POST.get('article_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog:detail', kwargs={'slug':slug}))


def article_index(request):
    articles = Article.objects.all().order_by('-pub_date')
    context = {'articles': articles}
    return render(request, 'blog/article_index.html', context)



def article_detail(request, slug):
    this_article = get_object_or_404(Article, slug=slug)
    total_likes = this_article.total_likes()
    comments = this_article.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = this_article
            new_comment.save()
    
    else:
        comment_form = CommentForm()

    return render(request, 'blog/article_detail.html', context={  
                                                                'this_article': this_article,
                                                                'comments':comments, 
                                                                'new_comment':new_comment, 
                                                                'comment_form':comment_form,
                                                                'total_likes': total_likes,
                                                                }
)