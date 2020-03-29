from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.


class Question(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    details = models.TextField(max_length=200)
    date_asked = models.DateTimeField(default=timezone.now)
    venue = models.CharField(max_length=200)
    date = models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.')
    time = models.TimeField(help_text='Please use the following format: <em>HH:MM:SS<em>')
    #attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attending', blank=True)
    num_of_attendees = models.PositiveIntegerField(default=0, blank=True)

    def __str__(self):
        return self.name