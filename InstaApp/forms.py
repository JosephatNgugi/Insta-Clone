from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserPost,Comment

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class PostForm(forms.ModelForm):
	"""Post model form"""

	class Meta:
		"""Form settings."""
		model = UserPost
		fields = ('caption', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['related_post', 'name' , 'created_on']