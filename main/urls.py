from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('api/status/', views.api_status, name='api_status'),
    path('api/posts/', views.api_posts, name='api_posts'),
]
