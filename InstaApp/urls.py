from django.urls import path

from . import views

urlpatterns =[
    path('signup/', views.UserRegistration, name='signup'),
    path('', views.home, name='home'),
]