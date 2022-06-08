from django.urls import path, include

from . import views

urlpatterns =[
    path('accounts/Sign-Up/', views.UserRegistration, name='signup'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/login/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    
]