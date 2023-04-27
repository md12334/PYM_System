from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import loader
from .decorators import *
from .forms import StaffRegForm, StudentRegForm
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import logging

# init
logger = logging.getLogger(__name__)


# ################################################ Custom Login functionality

def custom_login(request):
    """ custom login function that inherits django different auth functionality"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        logger.error("in custom login")

        if user is not None:
            login(request, user)
            if user.is_admin:
                logger.error("In custom logging")
                return redirect('/admin')
            elif user.is_staff:
                return redirect('/staff')
            elif user.is_student:
                return redirect('/student')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    # show message if trying to access a page that not permitted
    if 'next' in request.GET:
        logger.error("in next method")
        messages.error(request, 'Please login to access the page')

    return render(request, 'registration/login.html')


# # ############################################ # # General Section

# ROOT URL ""


# admin home
@admin_required
def index(request):
    total_staff = User.objects.filter(is_staff=True).count()
    total_student = User.objects.filter(is_student=True).count()
    total_course = Course.objects.all().count()
    total_submission = Submission.objects.all().count()
    total_notices = Notice.objects.all().count()
    logger.error("in admin home/index")
    return render(request=request, template_name="admin-home.html", context={
        "total_staff": total_staff,
        "total_student": total_student,
        "total_course": total_course,
        "total_submission": total_submission,
        "total_notices": total_notices,
    })


# activate staff
@admin_required()
def activate_user(request, id):
    user = User.objects.get(pk=id)
    user.is_active = True
    user.save()
    if user.is_staff:
        return redirect('show-staff')
    else:
        return redirect('show-student')


# deactivate staff
@admin_required()
def deactivate_user(request, id):
    user = User.objects.get(pk=id)
    user.is_active = False
    user.save()
    if user.is_staff:
        return redirect('show-staff')
    else:
        return redirect('show-student')


# # ############################################ # # Staff Section


# Add Staff
@admin_required()
def add_staff(request):
    if request.method == "POST":
        form = StaffRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_student = False
            user.staff = True
            user.admin = False
            user.save()

            messages.success(request, "Registration successful.")
            return redirect("add-staff")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = StaffRegForm()
    return render(request=request, template_name="add-staff.html", context={"register_form": form})


# Update Staff
@admin_required()
def update_staff(request, id):
    user = User.objects.get(pk=id)

    if request.method == "POST":
        form = StaffRegForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('show-staff')
    else:
        form = StaffRegForm(instance=user)
        return render(request=request, template_name="update-staff.html", context={"register_form": form})

# Show Staff
@admin_required()
def show_staff(request):
    users = User.objects.all()
    return render(request=request, template_name="show-staff.html", context={"users": users})


# Delete Staff
@admin_required()
def delete_staff(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('show-staff')


# # ############################################ # # Student Section


# Add student
@admin_required()
def add_student(request):
    if request.method == "POST":
        form = StudentRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_student = True
            user.staff = False
            user.admin = False
            user.save()
            messages.success(request, "Registration successful.")
            return redirect("add-student")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = StaffRegForm()
    return render(request=request, template_name="add-student.html", context={"register_form": form})


# Add student bulk
@admin_required()
def add_student_bulk(request):
    # get file from request and process the csv file to create users
    # todo
    return render(request=request, template_name="add-student-bulk.html")


# Show student
@admin_required()
def show_student(request):
    users = User.objects.all()
    return render(request=request, template_name="show-student.html", context={"users": users})


# Update student
@admin_required()
def update_student(request, id):
    user = User.objects.get(pk=id)

    if request.method == "POST":
        form = StudentRegForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('show-student')

    else:
        form = StudentRegForm(instance=user)
        return render(request=request, template_name="update-student.html", context={"register_form": form})


# Delete student
@admin_required()
def delete_student(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('show-student')


# # ############################################ # # Notice  and message Section


# show notice
@admin_required()
def show_notice(request):
    notices = Notice.objects.all()
    return render(request=request, template_name="show-notice.html", context={"notices": notices})


# show message
@admin_required()
def show_message(request):
    messages = Message.objects.all()
    return render(request=request, template_name="show-message.html", context={"messages_list": messages})


# # ############################################ # # Submission sections


@admin_required()
def show_submission(request):
    submissions = Submission.objects.all()
    return render(request=request, template_name="show-submission.html", context={"submissions": submissions})


@admin_required()
def update_submission(request, id):
    # todo
    return redirect('show-submission')
