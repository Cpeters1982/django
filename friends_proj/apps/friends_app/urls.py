from . import views
from django.conf.urls import url
def test(request):
	print 'in friends'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/(?P<id>\d+)$', views.profile),
    url(r'^users/add/(?P<id>\d+)$', views.add_friend),
    url(r'^users/remove/(?P<id>\d+)$', views.remove_friend),

]
