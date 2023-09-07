from django.urls import path
from . import views

urlpatterns = [
    path('login', views.members, name='members'),
    path('Register/', views.Register, name='Register'),
]
