from __future__ import unicode_literals
from ..login_app.models import User

from django.db import models

# Create your models here.
class CatManager(models.Manager):
	def createCat(self, postData):
		results  = {'status': True, 'errors': [], 'cat': None}
		if len(postData['name']) < 2:
			results['status'] = False
			results['errors'].append('This cats name is to short meow.')
		if len(postData['age']) < 1:
			results['status'] = False
			results['errors'].append('This cats age is to short meow.')

		if results['status'] == True:
			print postData['user_id'], '**********'
			userInt = int(postData['user_id'])
			user = User.objects.get(id = userInt)
			results['cat'] = Cat.objects.create(name = postData['name'], age = postData['age'], owner = user)
		return results
class Cat(models.Model):
	name = models.CharField(max_length = 50)
	age = models.CharField(max_length = 50)
	owner= models.ForeignKey(User , default= None)
	likes = models.IntegerField(default = 0)
	objects = CatManager()