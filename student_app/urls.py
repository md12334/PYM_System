from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='student-home'),
    path('profile', views.student_profile, name='student-profile'),
    path('view-course-student/<int:id>', views.view_course_student, name='view-course-student'),
]