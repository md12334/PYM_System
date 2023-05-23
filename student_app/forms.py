from django import forms
from django.contrib.auth import get_user_model
from django import forms
from admin_app.models import Course, User
from django.contrib.auth import get_user


# Staff update form
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'first_name',
            'last_name',
            'email',
            'department',
            'phone_number',
            'address',
        ]