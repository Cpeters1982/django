# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib  import messages
import bcrypt
import re

# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': True, 'errors': []}
        user = []
        if not postData['f_name'] or len(postData['f_name']) < 2:
            # print 'asjaJKFBjkadfbjkhHAB'
            results['status'] = False
            results['errors'].append('First name must be two or more characters.')
        if not postData['l_name'] or len(postData['l_name']) < 2:
            # print 'asjaJKFBjkadfbjkhHAB'
            results['status'] = False
            results['errors'].append('Last name must be two or more characters.')
        if not postData['email'] or len(postData['email']) < 4 or not re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        postData['email']):
            # print 'asjaJKFBjkadfbjkhHAB'
            results['status'] = False
            results['errors'].append('Email is not valid.')
        if not postData['password'] or len(postData['password']) < 5 or postData['password'] != postData['c_password']:
            # print 'asjaJKFBjkadfbjkhHAB'
            results['status'] = False
            results['errors'].append('Please confirm your password is 8 characters long and matches your confirmation password')
        if results['status'] == True:
            user = User.objects.filter(email = postData['email'])
        if len(user) != 0:
            results['status'] = False
            results['errors'].append('Please try another email.')
        return results

    def loginVal(self, postData):
        # print postData
        results = {'status': True, 'errors': [], 'user': None}
        if  len(postData['email']) < 3:
            results['errors'].append('Something went wrong! Please check your information and try again.')
            results['status'] = False
        else:
            user = User.objects.filter(email = postData['email'])
            if len(user) <= 0:
                results['errors'].append('Something went wrong! Please check your information and try again.')
                results['status'] = False
            elif len(postData['password']) < 5 or postData['password'] != user[0].password:
                results['errors'].append('Something went wrong! Please check your information and try again.')
                results['status'] = False
            else:
                results['user'] = user[0]
        return results



class User(models.Model):
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    objects = UserManager()
