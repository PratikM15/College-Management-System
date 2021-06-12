from django.db import models


# Create your models here.
class Student(models.Model):
    rollid = models.CharField(max_length=50, default="")
    passwd = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    branch = models.CharField(max_length=50, default="")
    year = models.CharField(max_length=50, default="")
    cgpa = models.CharField(max_length=15, default="")
    mob = models.CharField(max_length=15, default="")
    address = models.CharField(max_length=200, default="")
    dob = models.CharField(max_length=20, default="")

    class Meta:
        db_table = "student"

    def __str__(self):
        return self.name


class Professor(models.Model):
    roll = models.CharField(max_length=50, default="")
    passwd = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    salary = models.CharField(max_length=15, default="")
    mob = models.CharField(max_length=15, default="")
    address = models.CharField(max_length=200, default="")
    post = models.CharField(max_length=200, default="")
    dob = models.CharField(max_length=20, default="")

    class Meta:
        db_table = "professor"

    def __str__(self):
        return self.name
