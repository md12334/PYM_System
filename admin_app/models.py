from django.db import models
from django.contrib.auth.models import AbstractUser


# Main User Account Model - for superuser, admin, staff, students
class User(AbstractUser):

    # set metadata
    class Meta:
        db_table = "user"

    # User Types
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    # common columns
    department = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=255, unique=True, null=True)
    address = models.TextField(null=True)
