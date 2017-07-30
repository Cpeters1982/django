from . import views
from django.conf.urls import url
def test(request):
	print 'in cat'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addform$', views.addForm),
    url(r'^addcat$', views.addCat),
    url(r'^like/(?P<id>\d+)$', views.likeCat),



]
