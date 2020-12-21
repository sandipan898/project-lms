from django.shortcuts import render
from .models import Course, Student, Instructor, Game
from django.views import generic

# Create your views here.


# def show_user_view(request):
#     template_name = 'templates/api/user_info.html'
#     render(request, template_name)


# def home_view(request):
#     template_name = "api/home.html"
#     return render(request, template_name)

class HomeView(generic.View):
    template_name = "api/home.html"

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

# def dashboard_view(request):
#     template_name = "api/dashboard.html"
#     return render(request, template_name)


class DashboardView(generic.View):
    template_name = "api/dashboard.html"
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

# def course_list_view(request):
#     template_name = "api/courseslist.html"
#     courses = Course.objects.all()
#     context = {"courses": courses}
#     return render(request, template_name, context=context)


class CourseListView(generic.ListView):
    template_name = "api/courseslist.html"
    context_object_name = 'courses'
    queryset = Course.objects.all()

# def games_list_view(request):
#     template_name = "api/gameslist.html"
#     return render(request, template_name)


class GamesListView(generic.ListView):
    template_name = "api/gameslist.html"
    context_object_name = 'games'
    queryset = Game.objects.all()


def user_profile_view(request):
    template_name = "api/user_profile.html"
    return render(request, template_name)

