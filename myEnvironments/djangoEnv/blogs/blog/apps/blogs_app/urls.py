from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^new/', views.new),     # This line has changed!
    url(r'^create/', views.create),     # This line has changed! 
    url(r'^blogs/(?P\d+)', views.show),    # This line has changed!
    url(r'^blogs/(?P[0-9]{2})/edit', views.edit),     # This line has changed!
    url(r'^blogs/(?P[0-9]{2})/delete', views.destroy),     # This line has changed!
]
