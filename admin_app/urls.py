from django.urls import path, include
from . import views

urlpatterns = [

    # home
    path('', views.home, name='home'),

    # crud operation staff
    path('add-staff', views.add_staff, name='add-staff'),
    path('show-staff', views.show_staff, name='show-staff'),
    path('update-staff/<int:id>', views.update_staff, name='update-staff'),
    path('delete-staff/<int:id>', views.delete_staff, name='delete-staff'),

    # crud operation student
    path('add-student', views.add_student, name='add-student'),
    path('show-student', views.show_student, name='show-student'),
    path('update-student/<int:id>', views.update_student, name='update-student'),
    path('delete-student/<int:id>', views.delete_student, name='delete-student'),

    # function
    path('activate/<int:id>', views.activate_user, name='activate'),
    path('deactivate/<int:id>', views.deactivate_user, name='deactivate'),

    # auth
    path('', include("django.contrib.auth.urls")),
]
