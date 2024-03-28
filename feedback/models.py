from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_type = models.CharField(max_length=100)
    feedback_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.user.username} ({self.feedback_type})"
