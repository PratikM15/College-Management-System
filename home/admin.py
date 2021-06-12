from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Professor
admin.site.register(Student)
admin.site.register(Professor)