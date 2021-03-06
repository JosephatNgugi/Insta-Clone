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
    
    @receiver(post_save, sender=user)
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
    
    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/post/{self.id}"

    @property
    def get_all_comments(self):
        return self.comments.all()

    def total_likes(self):
        return self.likes.count()
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return f'{self.user.caption} Post'
    
# Comments Models
class Comment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.user.name} Comment'

# Follow Models
class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.follower} Follow'
