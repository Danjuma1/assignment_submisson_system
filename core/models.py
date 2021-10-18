from django.db import models
from django.utils import timezone

from accounts.models import User


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=8)
    lecturer_name = models.CharField(max_length=50)
    course_description = models.TextField()
    created_at = models.DateField(default=timezone.now)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.course_code + " : " + self.course_title

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    marks = models.CharField(max_length=20)
    deadline = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class AssignmentSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    matric_no = models.CharField(max_length=8)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.matric_no

