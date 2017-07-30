# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib  import messages
import bcrypt
import re

# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': True, 'errors':[]}
        user = []
        if not postData['fname'] or len(postData['fname']) < 2:
            results['status'] = False
            results['errors'].append['First name must be 2 or more characters']
        if not postData['lname'] or len(postData['lname']) < 2:
            results['status'] = False
            results['errors'].append['Last name must be 2 or more characters']
        if not postData['email'] or not re.match(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",
        postData['email']):
            results['status'] = False
            results['errors'].append['Email invalid. Please try again.']
        if not postData['password'] or len(postData['password']) < 5 or postData['password'] != postData['cpassword']:
            results['status'] = False
            results['errors'].append['Password is invalid. Please try again.']
        if results['status'] is False:
            return results
        user = User.objects.filter(email=postData['email'])
        if user:
            results['status'] = False
            results['errors'].append("Registration Failure, have you tried to login?")
        if results['status']:
            password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = User.objects.create(
                fname=postData['fname'],
                lname=postData['lname'],
                email=postData['email'],
                password=password)
            results['user'] = user
        return results

    def loginVal(self, postData):
        results = {'status': True, 'errors': [], 'user': None}
        user = User.objects.filter(email=postData['email'])
        try:
            user[0]
        except IndexError:
            results['status'] = False
            results['errors'].append("Account or password failure.")
            return results
        if user[0]:
            if user[0].password != bcrypt.hashpw(postData['password'].encode(),
                                                     user[0].password.encode()):
                results['status'] = False
                results['errors'].append("Account or password failure.")
            else:
                results['user'] = user[0].id
        else:
            results['status'] = False
        return results
    # 
    # def createUser(self, postData):
    #     password = bcrypt.hashpw(postData['Password'].encode(), bcrypt.gensalt())
    #     User.objects.create(fname= postData['fname'], lname= postData['lname'],email= postData['email'],)


class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
