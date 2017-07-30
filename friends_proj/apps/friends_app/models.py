# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

# # Create your models here.
# # class friends(models.Model):
# #     friend = models.ManyToManyRel(User)
# #     friend_id = models.CharField(max_length=65)
# #     created_at = models.DateTimeField(auto_now_add=True)
# class Friends(models.Model):
# 	# name = models.CharField(max_length = 50)
# 	# age = models.CharField(max_length = 50)
# 	friend = models.ForeignKey(User , default= None)
# 	# likes = models.IntegerField(default = 0)
# 	# objects = CatManager()
def addFriend(self, user_id, friend_id):
    user = self.get(id=user_id)
    friend = self.get(id=friend_id)
    Friend.objects.create(user_friend=user, second_friend=friend)
    Friend.objects.create(user_friend=friend, second_friend=user)

def removeFriend(self, user_id, friend_id):
    user = self.get(id=user_id)
    friend = self.get(id=friend_id)
    friendship1 = Friend.objects.get(user_friend=user, second_friend=friend)
    friendship2 = Friend.objects.get(user_friend=friend, second_friend=user)
    friendship1.delete()
    friendship2.delete()


class Friend(models.Model):
    user_friend = models.ForeignKey(User, related_name='requester')
    second_friend = models.ForeignKey(User, related_name='accepter')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
