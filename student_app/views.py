import logging
from django.shortcuts import render
from admin_app.decorators import student_required
from admin_app.models import *

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