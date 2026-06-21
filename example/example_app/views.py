from django.shortcuts import render


def home(request):
    return render(request, "example_app/home.html")
