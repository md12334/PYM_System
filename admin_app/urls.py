from django.urls import path, include
from . import views

urlpatterns = [

    # home
    path('', views.home, name='home'),

    # crud operation
    path('add-staff', views.add_staff, name='add-staff'),
    path('show-staff', views.show_staff, name='show-staff'),
    path('update-staff', views.update_staff, name='update-staff'),
    path('delete-staff', views.delete_staff, name='delete-staff'),

    # function
    path('activate/<int:id>', views.activate_staff, name='activate'),
    path('deactivate/<int:id>', views.deactivate_staff, name='deactivate'),

    # auth
    path('', include("django.contrib.auth.urls")),
]
