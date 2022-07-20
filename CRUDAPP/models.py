from django.db import models


# Create your models here.
class Student(models.Model):
    StudentName = models.CharField(max_length=200)
    StudentGender = models.CharField(max_length=10)
    StudentEmail = models.EmailField()
    StudentScore = models.PositiveSmallIntegerField()
