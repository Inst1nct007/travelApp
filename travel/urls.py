from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='travel-home'),
    path('international/', views.international, name='travel-international'),
    path('domestic/', views.domestic, name='travel-domestic'),
]