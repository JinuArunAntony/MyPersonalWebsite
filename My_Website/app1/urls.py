from django.template.defaulttags import url

from app1 import views
from django.urls import path

urlpatterns = [
    path("", views.home_fun,name="home"),
    path("about/", views.about_fun,name="about"),
    path("contact/", views.contact_fun,name="contact"),
    path("profile/", views.profile_fun,name="profile")
]