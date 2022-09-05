from django.http import HttpResponse
from django.template import loader
from .decorators import *
from django.shortcuts import render, redirect
from .forms import StaffRegForm, StudentRegForm
from django.contrib.auth import login
from django.contrib import messages
from .models import User


# admin home
@admin_required
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


# activate staff
@admin_required()
def activate_staff(request, id):
    user = User.objects.get(pk=id)
    user.is_active = True
    user.save()
    return redirect('show-staff')


# deactivate staff
@admin_required()
def deactivate_staff(request, id):
    user = User.objects.get(pk=id)
    user.is_active = False
    user.save()
    return redirect('show-staff')


# Add Staff
@admin_required()
def add_staff(request):
    if request.method == "POST":
        form = StaffRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("add-staff")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = StaffRegForm()
    return render(request=request, template_name="add-staff.html", context={"register_form": form})


# Show Staff
@admin_required()
def show_staff(request):
    users = User.objects.all()
    return render(request=request, template_name="show-staff.html", context={"users": users})


# Update Staff
@admin_required()
def update_staff(request, id):
    user = User.objects.get(pk=id)

    if request.method == "POST":
        form = StaffRegForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = StaffRegForm(instance=user)
        return render(request=request, template_name="update-staff.html", context={"register_form": form})


# Delete Staff
@admin_required()
def delete_staff(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('show-staff')


# Add student
@admin_required()
def add_student(request):
    if request.method == "POST":
        form = StudentRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("add-student")
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = StaffRegForm()
    return render(request=request, template_name="add-student.html", context={"register_form": form})


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
        form = StaffRegForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = StaffRegForm(instance=user)
        return render(request=request, template_name="update-student.html", context={"register_form": form})


# Delete student
@admin_required()
def delete_student(request, id):
    user = User.objects.get(pk=id)
    user.delete()
    return redirect('show-student')