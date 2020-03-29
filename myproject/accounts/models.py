from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)   #on deleting user,profile deleted but not vice versa
    image=models.ImageField(blank=True,upload_to='profile_pics')
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def get_date_of_birth(self):
        return self.date_of_birth

