import pathlib

from django.shortcuts import render


def home_view(request):
    html_template = "home.html"
    context = {
        "title": "Home page"
    }
    return render(request, html_template, context)
