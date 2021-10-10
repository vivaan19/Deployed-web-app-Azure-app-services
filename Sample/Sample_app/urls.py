from django.contrib import admin
from django.urls import path
from Sample_app import views
urlpatterns = [
    path("", views.index, name="Sample_app"),
    path("about", views.about, name="Sample_app"),
    path("contact", views.contact, name="Sample_app")
]
