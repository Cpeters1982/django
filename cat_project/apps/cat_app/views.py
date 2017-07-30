from django.shortcuts import render,redirect
from models import Cat
from ..login_app.models import User
from django.contrib import messages

def genErrors(request, Emessages):
	for message in Emessages:
		messages.error(request, message)
# Create your views here.
def checkUser(request):
	try:
		if request.session['f_name'] < 2:
			return False
		else:
			return True
	except:
		return False

def index(request):
	# User.objects.all().delete()
	# Cat.objects.all().delete()


	results = checkUser(request)
	if results == False:
		return redirect('/')
	context = {
	'cats': Cat.objects.all().order_by('-likes')
	}

	return render( request, 'cat_app/index.html', context)

def addForm(request):
	results = checkUser(request)
	if results == False:
		return redirect('/')
	return render( request, 'cat_app/addForm.html')
def addCat(request):
	results = checkUser(request)
	if results == False:
		return redirect('/')

	results = Cat.objects.createCat(request.POST)
	if results['status'] == False:
		genErrors(request, results['errors'])
		return redirect('/cats/addform')
	else:
		messages.success(request, 'New cat added!')
	return redirect('/cats')
def likeCat(request, id):
	try:
		cat = Cat.objects.get(id = id)
		cat.likes += 1
		cat.save()
		return redirect('/cats')
	except:
		return redirect('/')
