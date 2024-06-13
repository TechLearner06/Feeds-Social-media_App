from django.urls import path
from .import views

urlpatterns = [
    path('',views.loginPage,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('index',views.feeds,name='index'),
    path('profile',views.profile,name='edit_profile'),
    path('friends_list',views.feeds,name='followers'),

  
]
