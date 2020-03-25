from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Question(models.Model):
    text = models.TextField(max_length=200)
    date_asked = models.DateTimeField(default=timezone.now)
    #upvotes=models.IntegerField(default=0) 
    #asked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=0)
    def __str__(self):
        return self.text 