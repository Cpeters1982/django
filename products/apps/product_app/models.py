# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    weight = models.CharField(max_length=5)
    price = models.CharField(max_length=5)
    category = models.CharField(max_length=40)
