from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^register/$', views.register),    # This line has changed!
    url(r'^new/$', views.new),    # This line has changed!
    url(r'^validate/$', views.validate),    # This line has changed!
    url(r'^users/$', views.users),  
    url(r'^users/(?P<user_id>\d+)/edit', views.edit),
    url(r'^users/(?P<user_id>\d+)/delete', views.delete),

    # url(r'^$', views.index, name='index'),
    # url(r'^create/$', views.create, name="create"),
    # url(r'^new/$', views.new, name="new"),
    # url(r'^(?P<user_id>\d+)/show$', views.show, name="show"),
    # url(r'^logout/$', views.logout, name='logout'),
    # url(r'^login/$', views.login, name='login'),
    # url(r'^(?P<user_id>\d+)/edit', views.edit, name="edit"),
    # url(r'^(?P<user_id>\d+)/delete', views.delete, name="delete"),
    # url(r'^(?P<user_id>\d+)/update', views.update, name="update"),

]
