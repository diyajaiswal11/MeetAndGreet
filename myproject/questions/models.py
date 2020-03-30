from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Question(models.Model):
    text = models.TextField(max_length=50)
    date_asked = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text