# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    context = {
    'email' : 'blob@blob.com',
    'name' : 'Chris'
    }
    return render(request, 'second_app/index.html', context)

def show(request, id):
    context = {
    'id' : id
    }
    return render(request, 'second_app/show.html', context)
