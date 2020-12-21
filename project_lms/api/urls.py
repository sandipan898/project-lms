from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('profile/', user_profile_view, name="profile"),
    path('courses/', CourseListView.as_view(), name="courses-list"),
    path('games/', GamesListView.as_view(), name="games-list"),
]