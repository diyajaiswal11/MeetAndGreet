from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    text = models.TextField(max_length=50)
    date_asked = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text

"""
class Comment(models.Model):
    event = models.ForeignKey(Question, related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    """