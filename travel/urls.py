from django.urls import path
from . import views
from .views import PlaceListView, details

urlpatterns = [
    path('', PlaceListView.as_view(), name='travel-home'),
    path('place/<int:pk>/', details, name='place-details'),
    path('international/', views.international, name='travel-international'),
    path('domestic/', views.domestic, name='travel-domestic'),
    path('about/', views.about, name='travel-about'),
]