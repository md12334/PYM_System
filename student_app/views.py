from django.shortcuts import render
from django.http import HttpResponse

from admin_app.decorators import student_required


# Student Home
@student_required
def index(request):
    return HttpResponse("Student Home")