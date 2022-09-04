from django.urls import path, include
from . import views as v
from .forms import *
from django.contrib.auth import views

urlpatterns = [
    path('', v.home, name='home'),
    path('', include("django.contrib.auth.urls")),
]
