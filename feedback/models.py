from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    fb_uname = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    fb_type = models.CharField(max_length=100)
    fb_content = models.TextField()
    fb_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.fb_uname.username} ({self.fb_type})"

