# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib  import messages
from models import User

# Create your views here.
def index(request):
    return render(request, "loginapp/index.html")

def register(request):
    results = User.objects.registerVal(request.POST)
    if results['status'] == False:
        # print '*'*50
        for error in results['errors']:
            messages.error(request, error)
    else:
        user = User.objects.create(f_name = request.POST['f_name'], l_name = request.POST['l_name'], email = request.POST['email'], password = request.POST['password'])
        print user

    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        return redirect('/')
