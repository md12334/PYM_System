from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import loader
from django.contrib.auth import authenticate, login
from .decorators import *


# Admin Home
@admin_required
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

