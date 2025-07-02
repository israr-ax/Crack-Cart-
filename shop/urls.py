from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="HomeShop"),
    path('about/', views.about, name="About"),
    path('contact/', views.contact, name="Contact Us"), 
    path('tracker/', views.tracker, name="Tracker"),
    path("productview/<int:myid>", views.productview, name="Product"),  
    path('checkout/', views.checkout, name="Checkout"),
    path('search/', views.search, name="Search"),
]




