from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse




class Article(models.Model):
    title = models.CharField(max_length = 100, unique = True)
    body = models.TextField()
    slug = models.SlugField(null=True)
    image = models.ImageField(default='default.jpg', blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



    def __str__(self) -> str:
        return self.title

    def snippet(self):
        return self.body[:100]
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})




class Comment(models.Model):
    post = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)



    def __str__(self) -> str:
        return f'Comment {self.body} by {self.name}'


    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})
    