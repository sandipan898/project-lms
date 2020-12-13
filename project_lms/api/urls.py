from django.urls import path, include
from .views import show_user_view

urlpatterns = [
    path('', show_user_view),
]