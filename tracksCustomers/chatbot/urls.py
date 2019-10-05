from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('store/', views.store, name="store"),
    path('question/', views.load_question, name="load_question"),
      
]
