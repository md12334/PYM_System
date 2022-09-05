from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-staff', views.add_staff, name='add-staff'),
    path('show-staff', views.show_staff, name='show-staff'),
    path('update-staff', views.update_staff, name='update-staff'),
    path('delete-staff', views.delete_staff, name='delete-staff'),
    path('', include("django.contrib.auth.urls")),
]
