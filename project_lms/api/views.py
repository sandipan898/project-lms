from django.shortcuts import render

# Create your views here.


def show_user_view(request):
    template_name = 'templates/api/user_info.html'
    render(request, template_name)