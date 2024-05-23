from django.urls import path 
from app import views

urlpatterns=[

 path('new/', views.new),
]