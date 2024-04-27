from django.contrib import admin
from django.urls import path
from  . import views

urlpatterns = [
    path('', views.first_page),
    path ('second/', views.second_page),
    path ('second/three/', views.three_page)
]
