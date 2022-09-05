from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


# staff reg form
class StaffRegForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "department",
            "phone_number",
            "address",
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super(StaffRegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True
        if commit:
            user.save()
        return user


# student reg form
class StudentRegForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "department",
            "phone_number",
            "address",
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super(StudentRegForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_student = True
        if commit:
            user.save()
        return user