from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'randomword$', views.randomword),
    url(r'^reset$', views.reset)     # This line has changed!
]
