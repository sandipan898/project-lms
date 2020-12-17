from django.urls import path, include
from .views import home_view, dashboard_view, course_list_view, games_list_view, user_profile_view

urlpatterns = [
    path('', home_view, name="home"),
    path('dashboard/', dashboard_view, name="dashboard"),
    path('profile/', user_profile_view, name="profile"),
    path('courses/', course_list_view, name="courses-list"),
    path('games/', games_list_view, name="games-list"),
]