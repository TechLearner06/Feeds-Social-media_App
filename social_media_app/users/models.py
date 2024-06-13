from django.db import models
from django.contrib.auth import get_user_model



#create your models here



class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images' , default='user_dp.jpg')
    location = models.CharField(max_length=100, blank=True)

