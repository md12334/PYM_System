from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from admin_app.decorators import staff_required
import logging

from admin_app.forms import StaffRegForm
from staff_app.forms import *

# logger
logger = logging.getLogger(__name__)


# Staff Home
@staff_required
def index(request):
    courses = Course.objects.filter(staff=request.user)
    logger.error("in admin home/index")
    return render(request=request, template_name="staff-home.html", context={
        "courses": courses
    })


# Staff Profile
@staff_required
def staff_profile(request):
    logger.error("in staff profile method")

    if request.method == "POST":
        form = StaffUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            logger.error("in staff profile: is_valid")

            return redirect('staff-profile')
    else:
        if 'reset' in request.GET and request.GET['reset']:
            form = StaffRegForm(instance=request.user)
        else:
            form = StaffUpdateForm(instance=request.user)
        return render(request=request, template_name="staff-profile.html", context={"register_form": form})


@staff_required
def create_course(request):
    logger.error("in staff course create method")

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save(authenticated_user=request.user)
            logger.error("in course details: is_valid")

            return render(request=request, template_name="staff-create-course.html", context={
                "course_form": form,
                "messages": ["Course created successfully.", ]
            })
        else:
            return render(request=request, template_name="staff-create-course.html", context={"course_form": form})

    else:
        form = CourseForm()
        return render(request=request, template_name="staff-create-course.html", context={"course_form": form})


@staff_required()
def update_course(request, id):
    course = Course.objects.get(pk=id)

    if request.user != course.staff:
        return render(request=request, template_name="update-course.html", context={
            "messages": ["Sorry you can't access other staff's course"]
        })

    elif request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save(authenticated_user=request.user)
        return render(request=request, template_name="update-course.html", context={
            "course_form": form,
            "messages": ["Course Updated Successfully"]
        })

    else:
        form = CourseForm(instance=course)
        return render(request=request, template_name="update-course.html", context={"course_form": form})


@staff_required()
def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect("staff-home")


@staff_required()
def view_course(request, id):
    course = Course.objects.get(id=id)
    return render(request=request, template_name="view-course.html", context={"course": course})


@staff_required()
def add_students(request, id):
    if request.method == 'POST':

        form = EnrollForm(request.POST)
        if form.is_valid():
            students = list(form.cleaned_data['students'])
            students_id = [student.id for student in students]

            course = Course.objects.get(id=id)
            for student_id in students_id:
                course.students.add(User.objects.get(id=student_id))

            # Do something with the selected students
            return redirect('view-course',id)
    else:
        form = EnrollForm()
    return render(request, 'add-students.html', {'form': form, "course_id": id})


@staff_required()
def remove_student(request):
    logger.error("In Remove Student")
    if request.method == 'POST':
        course_id = request.POST['course_id']
        student_id = request.POST['student_id']

        course = Course.objects.get(id=course_id)
        student = User.objects.get(id=student_id)
        course.students.remove(student)

        logger.error(course)
        logger.error(student)
        return redirect('view-course', course_id)
