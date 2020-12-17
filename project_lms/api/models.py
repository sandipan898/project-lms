from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=30, blank=True)
    phone_no = models.CharField(max_length=15, blank=True, null=True)

    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        student_profile = Student.objects.create(user=instance)
        student_profile.save()
        

class Course(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    prereq = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    student = models.ManyToManyField('Student',  blank = True, related_name = ('StudentCourses'))
    instructor = models.ManyToManyField('Instructor' , blank = True , related_name = ('CourseTutor'))

    def __str__(self):
        return self.name

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=30, blank=True)
    profession = models.TextField(blank=True, null=True)
    
    def __str__(self):
            return self.user.username
    
    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name


@receiver(post_save, sender=User)
def create_instructor(sender, instance, created, **kwargs):
    if created:
        instructor_profile = Instructor.objects.create(user=instance)
        instructor_profile.save()
