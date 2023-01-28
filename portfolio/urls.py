from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('contact', views.contact, name = "contact"),
    path('projects', views.projects, name = "projects"),
    path('gallery', views.gallery, name = "gallery"),
]