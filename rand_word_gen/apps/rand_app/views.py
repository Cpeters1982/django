# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
import random


def index(request):
    print "*"*50
    return render(request, 'rand_app/index.html')
def randomword(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    word = ''
    my_letters = ['a','b','c','d','e','f','g','h','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']
    for times in range(0,14):
        word = word +str(random.choice(my_letters))
    words = {
        'random_word': word
    }
    return render(request, 'rand_app/index.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')
