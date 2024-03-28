from django.db import models

# Create your models here.

class ForumPost(models.Model):
    fp_title = models.CharField(max_length=200,)
    fp_content = models.TextField()
    fp_author = models.CharField(max_length=100,)
    fpcreated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
