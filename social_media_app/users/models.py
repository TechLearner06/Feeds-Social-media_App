from django.db import models
from django.contrib.auth import get_user_model



#create your models here

class Profile(models.Model):

    GENDER_CHOICES = [
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    id_user = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images' , default='user_dp.jpg')
    gender=models.CharField(max_length=6, choices=GENDER_CHOICES, default='other')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username