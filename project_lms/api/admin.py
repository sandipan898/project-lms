from django.contrib import admin
from .models import Student, Course, Instructor, Game
# Register your models here.

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Game)
