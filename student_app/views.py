import logging
from django.shortcuts import render, redirect
from admin_app.decorators import student_required
from admin_app.forms import StudentRegForm
from admin_app.models import *
from student_app.forms import StudentUpdateForm

# logger
logger = logging.getLogger(__name__)


# Student Home
@student_required
def index(request):
    courses = Course.objects.filter(students=request.user)
    logger.error("in student home/index")
    return render(request=request, template_name="student-home.html", context={
        "courses": courses
    })



# Student Profile
@student_required
def student_profile(request):
    logger.error("in staff profile method")

    if request.method == "POST":
        form = StudentUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            logger.error("in staff profile: is_valid")

            return redirect('student-profile')
    else:
        if 'reset' in request.GET and request.GET['reset']:
            form = StudentRegForm(instance=request.user)
        else:
            form = StudentUpdateForm(instance=request.user)
        return render(request=request, template_name="student-profile.html", context={"register_form": form})