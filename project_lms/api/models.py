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

    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name


@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()


class Course(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    prereq = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    student = models.ManyToManyField('Student', null = True, blank = True, related_name = _('Student courses'))


class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    about = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=30, blank=True)

    def get_full_name(self):
        full_name = self.first_name + " " + self.last_name
        return full_name


@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()
