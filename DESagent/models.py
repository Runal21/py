from django.db import models

# Create your models here.
class DESAgent(models.Model):
    cb_name = models.CharField(max_length=100)
    msg_des = models.TextField()
  
    def __str__(self):
        return self.name