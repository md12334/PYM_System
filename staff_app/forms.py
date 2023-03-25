from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from admin_app.forms import StaffRegForm


# @login_required
class StaffUpdateForm(forms.ModelForm):

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
