# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.contrib import messages
# from .models import User

# Create your views here.
def index(request):
    # print '*'*50
    return render(request, 'login_app/index.html')
