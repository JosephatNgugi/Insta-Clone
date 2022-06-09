from django.urls import path, include

from . import views

urlpatterns =[
    path('accounts/Sign-Up/', views.UserRegistration, name='signup'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('user/(\d+)/', views.user, name='users'),
    path('new/image', views.new_post, name='new_post'),
    path('comments/(\d+)/', views.comments, name='comments'),
    path('like/(\d+)/',views.like_post, name='like' ),
]