from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='staff-home'),
    path('profile', views.staff_profile, name='staff-profile'),
    path('create-course', views.create_course, name='create-course'),
    path('update-course/<int:id>', views.update_course, name='update-course'),
    path('delete-course/<int:id>', views.delete_course, name='delete-course'),
    path('view-course/<int:id>', views.view_course, name='view-course'),
    path('add-students/<int:id>', views.add_students, name='add-students'),
    path('remove-students', views.remove_student, name='remove-students'),
]