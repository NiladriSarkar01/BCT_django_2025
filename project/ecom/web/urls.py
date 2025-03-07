from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart', views.cart, name="cart"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('profile', views.profile, name="profile"),
    path('products', views.product, name="product")
]