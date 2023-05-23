from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='student-home'),
    path('profile', views.student_profile, name='student-profile'),
]