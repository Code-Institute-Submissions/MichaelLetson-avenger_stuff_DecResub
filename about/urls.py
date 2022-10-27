from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('contact/', views.contact_us, name='contact_us'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('reviews/', views.review, name='review'),
    path('delete/<review_id>', views.delete_review, name='delete_review'),
]
