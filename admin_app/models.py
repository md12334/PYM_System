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


# Course model with teacher_id, students, course_name, course_code, course_description, course_credit
class Course(models.Model):
    class Meta:
        db_table = "course"

    # columns
    course_name = models.CharField(max_length=100, null=False)
    course_code = models.CharField(max_length=100, null=False, unique=True)
    course_description = models.TextField(null=True)
    course_credit = models.IntegerField(null=False)

    staff = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    students = models.ManyToManyField(User, related_name="students", blank=True)

    # return course name
    def __str__(self):
        return self.course_name


# Submission model with student_id, course_id, submission_date, submission_file, submission_description
class Submission(models.Model):
    class Meta:
        db_table = "submission"

    # columns
    submission_date = models.DateTimeField(auto_now_add=True)
    submission_file = models.FileField(upload_to="submission_files/", null=False)
    submission_description = models.TextField(null=True)
    is_accepted = models.BooleanField(default=False)
    marks = models.IntegerField(null=True)

    student = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)

    # return submission file name
    def __str__(self):
        return self.submission_file.name


# Notice model with course_id, notice_date, notice_description
class Notice(models.Model):
    class Meta:
        db_table = "notice"

    # columns
    notice_date = models.DateTimeField(auto_now_add=True)
    notice_description = models.TextField(null=False)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)

    # return notice description
    def __str__(self):
        return self.notice_description


# Message model with sender_id, receiver_id, message_date, message_description
class Message(models.Model):
    class Meta:
        db_table = "message"

    # columns
    message_date = models.DateTimeField(auto_now_add=True)
    message_description = models.TextField(null=False)

    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name="receiver")

    # return message description
    def __str__(self):
        return self.message_description
