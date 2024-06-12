from django.contrib import admin
from django.urls import path
from . import views
from .views import homepage


# path to all the web pages, pretty self explanatory lmao
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('homepage/', views.homepage, name='home'),
    path('regattas/', views.regattas, name='regattas'),
    path('weather/', views.weather, name='weather'),
    path('login/', views.custom_login_view, name='login')
]
