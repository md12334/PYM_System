from django import forms
from django.contrib.auth import get_user_model
from django import forms
from admin_app.models import Course, User
from django.contrib.auth import get_user


# Staff update form
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


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_name',
            'course_code',
            'course_description',
            'course_credit'
        ]

    def save(self, authenticated_user, commit=True):
        """
        assign staff while saving the course
        :param authenticated_user:
        :param commit:
        :return:
        """
        course = super().save(commit=False)
        course.staff = authenticated_user
        if commit:
            course.save()
        return course


class EnrollForm(forms.Form):
    students = forms.ModelMultipleChoiceField(
        queryset=User.objects.filter(is_student=True),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        label='Students'
    )
