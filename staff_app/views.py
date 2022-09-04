from django.shortcuts import render
from django.http import HttpResponse


# Staff Home
def index(request):
    return HttpResponse("Staff Home")