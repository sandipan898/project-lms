from django.shortcuts import render
from .models import Course, Student, Instructor

# Create your views here.


# def show_user_view(request):
#     template_name = 'templates/api/user_info.html'
#     render(request, template_name)


def home_view(request):
    template_name = "api/home.html"
    return render(request, template_name)

def dashboard_view(request):
    template_name = "api/dashboard.html"
    return render(request, template_name)

def course_list_view(request):
    template_name = "api/courseslist.html"
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, template_name, context=context)

def games_list_view(request):
    template_name = "api/gameslist.html"
    return render(request, template_name)

def user_profile_view(request):
    template_name = "api/user_profile.html"
    return render(request, template_name)