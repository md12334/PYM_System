from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='staff-home'),
    path('profile', views.staff_profile, name='staff-profile'),
]