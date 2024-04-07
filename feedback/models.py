from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):
    fb_uname =models.ForeignKey(User, on_delete=models.CASCADE,default=None,related_name='fb_uname')
    fb_content = models.TextField()
    fb_timestamp = models.DateTimeField(auto_now_add=True)

class FeedbackReply(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def user_name(self):
        return self.feedback.fb_uname.username
