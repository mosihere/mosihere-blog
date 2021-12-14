from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class Article(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    body = models.TextField()
    slug = models.SlugField(null=True)
    image = models.ImageField(default='default.jpg', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='blog_posts')


    def __str__(self) -> str:
        return self.title

    def snippet(self):
        return self.body[:100]
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

    def total_likes(self):
        return self.likes.count()



class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']


    def __str__(self) -> str:
        return f'Comment {self.body} by {self.name}'