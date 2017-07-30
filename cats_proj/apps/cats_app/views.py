# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib  import messages
from models import User

# Create your views here.
def index(request):
    # print '*'*50
    return render(request, ('cats_app/index.html'))

def register(request):
    # print '********** Here I am at register ********'
    results = User.objects.registerVal(request.POST)
    if results['status'] == False:
        # print '*'*50
        for error in results['errors']:
            messages.error(request, error)
    else:
        user = User.objects.create(fname = request.POST['fname'], lname = request.POST['lname'], email = request.POST['email'], password = request.POST['password'])
        print user

    # return redirect('/')
    return render(request, ('cats_app/index.html'))

def login(request):
    # print "$$$$$ Login! $$$$$"
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        for error in results['errors']:
            messages.error(request, error)
        # return redirect('/')
    return render(request, ('cats_app/index.html'))
