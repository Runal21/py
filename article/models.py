from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone

class Article(models.Model):
    art_title = models.CharField(max_length=100)
    art_content = models.TextField()
    art_image = models.ImageField(upload_to='article_images',null=True, blank=True)
    art_author = models.CharField(max_length=20)
    art_created_at = models.DateTimeField(default=timezone.now)
