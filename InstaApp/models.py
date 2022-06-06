from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from PIL import Image

# Create your models here.

# UserProfiles Models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField('image file', upload_to='Insta/profilePics', default='static/images/default-profile.png')
    about = models.TextField(max_length=500, default='About Me', blank=True)
    name = models.CharField(max_length=60)
    following = models.ManyToManyField('UserProfile', blank=True)
    followers = models.ManyToManyField('UserProfile', blank=True)
    joined = models.DateTimeField(auto_now_add=True, default=timezone.now)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.UserProfile.save
        
# Posts Models
# Comments Models
# Likes Models
