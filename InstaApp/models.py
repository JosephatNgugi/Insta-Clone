from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# UserProfiles Models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField('image file', upload_to='Insta/profilePics', default='static/images/default-profile.png')
    about = models.TextField(max_length=500, default='About Me', blank=True)
    name = models.CharField(max_length=60)
    following = models.ManyToManyField('UserProfile', blank=True)
    followers = models.ManyToManyField('UserProfile', blank=True)
    
# Posts Models
# Comments Models
# Likes Models
