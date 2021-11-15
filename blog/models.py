from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.

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

