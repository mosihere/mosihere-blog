from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.article_index ,name='home'),
    path('<slug:slug>', views.article_detail, name='detail'),
    path('like/<slug:slug>', views.article_like, name='like_article'),
]
