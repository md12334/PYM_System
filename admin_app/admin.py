from django.contrib import admin
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'is_active', 'is_staff', 'is_student', 'department', 'phone_number', 'address')


#  register the model in the app’s admin.py
admin.site.register(User, UserAdmin)
admin.site.register(Course)
admin.site.register(Submission)
admin.site.register(Notice)
admin.site.register(Message)
