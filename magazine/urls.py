from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingPage, name="home"), 
    path('about/', views.aboutPage, name="about"),
    path('article/', views.articlepage, name="article"),
    path('category/', views.categorylist, name='category'),
    path('price/', views.pricepage, name="price"),
    path('register/', views.reg, name="register"),
    path('login/', views.login, name="login"),
    path('contact/', views.contactpage, name="contact"),
    path('magazine/', views.magpage, name="magazine")
]