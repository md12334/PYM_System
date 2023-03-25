from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

import logging

logger = logging.getLogger(__name__)


def admin_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged-in user is a teacher,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_admin,
        login_url="custom_login",
        redirect_field_name=redirect_field_name
    )
    # logger.error("admin_required")
    if function:
        return actual_decorator(function)
    return actual_decorator


def staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged-in user is a student,
    redirects to the log-in page if necessary.
    """
    # logger.error("staff_required")

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_staff,
        login_url="custom_login",
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def student_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Decorator for views that checks that the logged in user is a teacher,
    redirects to the log-in page if necessary.
    """
    # logger.error("student_required")

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_student,
        login_url="custom_login",
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
