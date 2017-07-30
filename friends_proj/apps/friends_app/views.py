# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login_app.models import User
from .models import Friend
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def friends(request):
    me = User.objects.get(id=request.session['id'])
    try:
        users = User.objects.all()
        others = []
        for other_user in users:
            if (other_user.id != request.session['id']):
                others.append(other_user)
    except:
        users = None

    try:
        friends = Friend.objects.filter(user_friend=me)
        real_friends = []
        for each_friend in friends:
            real_friends.append(each_friend.second_friend)
        real_others = []
        for other_user in others:
            if (other_user not in real_friends):
                real_others.append(other_user)
    except:
        friends = None

    context = {
        'me' : me,
        'users' : real_others,
        'friends' : real_friends
    }
    return render(request, 'friends.html', context)

def profile(request, id):
    profile = User.objects.get(id=id)
    context = {
        'user' : profile
    }
    return render(request, 'profile.html', context)

def add_friend(request, id):
    User.userManager.addFriend(request.session['id'], id)
    return redirect('friends')

def remove_friend(request, id):
    User.userManager.removeFriend(request.session['id'], id)
    return redirect('friends')
