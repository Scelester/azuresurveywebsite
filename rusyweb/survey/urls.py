from django.contrib import admin
from django.urls import path

from . import views

app_name = "survey"

urlpatterns = [
    path('',views.index,name='index'),
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name= "logout"),
    path("thanks", views.thanks_request, name="thanks"),
]
