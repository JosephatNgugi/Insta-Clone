from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from PIL import Image
from cloudinary.models import CloudinaryField

# Create your models here.

# UserProfiles Models
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = CloudinaryField('image', default='static/images/default-profile.png')
    about = models.TextField(max_length=500, default='About Me', blank=True)
    name = models.CharField(max_length=60)
    following = models.ManyToManyField('UserProfile', blank=True)
    followers = models.ManyToManyField('UserProfile', blank=True)
    joined = models.DateTimeField(default=timezone.now)
        
    def save_profile(self):
        """Method to save user details"""
        self.user

    def delete_profile(self):
        """Method to delete user details"""
        self.delete()
        
    # def update_profile(self,user_id, about, profile_pic):
    #     user = User.objects.get(id=user_id)
    #     self.about = about
    #     self.profile_pic = profile_pic
    #     self.save(user)

    @classmethod
    def search_profile(cls, name):
        """Method to Search for a user profile"""
        return cls.objects.filter(user__username__icontains=name).all()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        This method will automatically create a user profile using user details provided

        Args:
            sender (_type_): The sender of the signal. This will be triggered by the user
            instance (_type_): instance of user being created
            created (_type_): user profile to be created
        """
        if created:
            UserProfile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        """This method will save the userprofile instance created"""
        instance.UserProfile.save

    def __str__(self):
        return f'{self.user.username} Profile'
    
# Posts Models
class UserPost(models.Model):
    user = models.ForeignKey(UserProfile, on_delete= models.CASCADE, related_name='posts')
    image = CloudinaryField('image')
    caption = models.CharField(max_length=300, blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, blank=True)
    
# Comments Models
# Likes Models
