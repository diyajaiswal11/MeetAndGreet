from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)   #on deleting user,profile deleted but not vice versa
    firstname=models.CharField(max_length=200,null=True)
    lastname=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    profilepicture=models.ImageField(upload_to='profile_pics',default='default.jpg')
    date_of_birth = models.DateField(null=True,help_text='Please use the following format: <em>YYYY-MM-DD</em>.')

    def __str__(self):
        return f'{self.user.username} Profile'


