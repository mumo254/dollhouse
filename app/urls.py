
  
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/<int:id>', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]