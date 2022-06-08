from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):

        self.user = User.objects.create_user('testuser','password')
        self.profile = UserProfile(about='Testcase',profile_pic='', user=self.user,name='Test',following=1,follower=1)
        self.profile.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, UserProfile))

    def test_save_profile(self):
        self.profile.save_profile()
        after = UserProfile.objects.all()
        self.assertTrue(len(after)>0)