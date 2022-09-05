from django.http import HttpResponse
from django.template import loader
from .decorators import *
from django.shortcuts import render, redirect
from .forms import StaffRegForm
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
def update_staff(request):
    if request.method == "POST":
        pass

    form = StaffRegForm()
    return render(request=request, template_name="update-staff.html", context={"register_form": form})


# Delete Staff
@admin_required()
def delete_staff(request):
    if request.method == "POST":
        pass

    form = StaffRegForm()
    return render(request=request, template_name="delete-staff.html", context={"register_form": form})
