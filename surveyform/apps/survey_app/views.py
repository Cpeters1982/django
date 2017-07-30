# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    # print "*"*50
    return render(request, 'survey_app/index.html')

def formProcess(request):
    # print '*'*50
    # print 'we\'re at formProcess'
    # print '*'*50
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Name": request.POST['name'],
        "Dojo Location": request.POST['dojoLocation'],
        "Favorite Language": request.POST['favLang'],
        "Comments": request.POST['comments']
    }
    return redirect ('/showResults')

def showResults(request):
    # print request.session
    return render(request, 'survey_app/results.html')
