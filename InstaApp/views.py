from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, login, logout

from .models import UserPost, Comment
from .forms import *


# Create your views here.

def UserRegistration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            InputPassword = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=InputPassword)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration.html', {'form': form})

# @login_required(login_url='accounts/login/')
# def logout_user(request):
#     logout(request)
#     return redirect('accounts/login/')

@login_required(login_url='/accounts/login/')
def home(request):
    posts = UserPost.objects.all()
    number = Comment.objects.count()
    return render(request, 'Insta/home.html',{'posts':posts, 'number':number})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user.profile
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('home')
    else:
        form = PostForm()
    return render(request, 'Insta/new_post.html', {'form':form})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user.profile
    profPic = UserPost.objects.filter(user=current_user).all()
    return render(request, 'Insta/profile.html', {'profPic':profPic})

def user(request, user_id):
    users = User.objects.filter(id=user_id)
    profPic = UserPost.objects.filter(profile=user_id).all()    
    return render(request, 'Insta/user.html', {'profPic':profPic, 'users':users}) 

@login_required(login_url='accounts/login')
def comments(request, id):
    current_user = request.user.profile
    post = UserPost.objects.filter(id=id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post = post
            comment.save()
        return redirect('comments')
    else:
        form = CommentForm()

    userComment = Comment.objects.filter(post=id).all()
    return render(request, 'Insta/comments.html', {'userComment':userComment, 'form':form})

def like_post(request, post_id):
    current_user = request.user
    post = UserPost.objects.get(id=post_id)
    if post.likes.filter(id=current_user.id).exists():
        post.likes.remove(current_user)
    else:
        post.likes.add(current_user)
    return redirect('home')