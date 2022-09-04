from django.shortcuts import render
from django.http import HttpResponse


# Student Home
def index(request):
    return HttpResponse("Student Home")