from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.aboutus, name="about_us"),
    path('contact/', views.contactus, name="contact_us"),
    path('details/', views.details, name="details"),
    path('thanks/', views.helpful, name="thanks"),
]
