from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    semester = models.IntegerField()

class Student(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    courses = models.ForeignKey('Course', on_delete=models.CASCADE)
