from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

#  register the model in the app’s admin.py
admin.site.register(User, UserAdmin)
