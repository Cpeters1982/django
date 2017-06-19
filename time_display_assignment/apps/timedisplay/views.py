# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
    "datetime": datetime.today()
    }
    return render(request,'timedisplay/index.html', context)
