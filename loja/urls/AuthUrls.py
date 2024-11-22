from django.urls import path
from loja.views.AuthView import *
urlpatterns = [
    path("login", login_view, name='login'),
    path("register", register_view, name='register'),
]