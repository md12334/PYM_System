from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from admin_app.decorators import staff_required
import logging

from staff_app.forms import StaffUpdateForm

# logger
logger = logging.getLogger(__name__)


# Staff Home
@staff_required
def index(request):
    total_staff = 0
    total_student = 0
    total_course = 0
    total_submission = 0
    total_notices = 0
    logger.error("in admin home/index")
    return render(request=request, template_name="staff-home.html", context={
        "total_staff": total_staff,
        "total_student": total_student,
        "total_course": total_course,
        "total_submission": total_submission,
        "total_notices": total_notices,
    })


# Staff Profile
@staff_required
# @login_required
def staff_profile(request):
    logger.error("in staff profile method")

    if request.method == "POST":
        form = StaffUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            logger.error("in staff profile: is_valid")

            return redirect('staff-profile')
    else:
        form = StaffUpdateForm(instance=request.user)
        return render(request=request, template_name="staff-profile.html", context={"register_form": form})
