from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, login, logout

from .forms import SignUpForm


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

@login_required(login_url='accounts/login/')
def logout_user(request):
    logout(request)
    return redirect('accounts/login/')

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'Insta/home.html')