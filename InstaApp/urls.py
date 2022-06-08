from django.urls import path, include

from . import views

urlpatterns =[
    path('accounts/Sign-Up/', views.UserRegistration, name='signup'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.home, name='home'),
]