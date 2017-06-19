# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    # response = "hello"
    # return HttpResponse(response)
    return render(request, "django_portfolio/index.html")

def testimonials(request):
    return render(request, "django_portfolio/testimonials.html")

def about(request):
    return render (request, "django_portfolio/about.html")

def projects(request):
    return render(request, "django_portfolio/projects.html")


def create(request):
    request.session['name'] = request.POST['first_name']
    if request.method == "POST":
        print (request.POST)
    else:
        return redirect('/')
