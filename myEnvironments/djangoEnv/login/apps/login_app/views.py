# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request, "login_app/index.html")


def register(request):
    return render(request, "login_app/register.html")

def new(request):
    if request.method == "GET":
        return redirect('/register')
    if request.method == "POST":
        results = User.objects.basic_validator(request.POST)
        if isinstance(results, dict):
            for tag, error in results.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/register')
        else:
            print "*" * 80
            request.session['user_id'] = results
            return redirect('/users')

def users(request):
    if "user_id" in request.session:
        context = {
            'users': User.objects.all()
        }
        return render(request, "login_app/users.html", context)
    else:
        return redirect('/')

    
def validate(request):
    if request.method == "POST":
        results = User.objects.login_user(request.POST)
        print results
        print "*" * 80
        print type(results)
        if isinstance(results, dict):
            for tag, error in results.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            request.session['user_id'] = results
            return redirect('/users')
    else:
        return redirect('/')

def edit(request, user_id):
    user = User.objects.get(id = user_id)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'id': user.id
    }
    return render(request, "login_app/users.html", context)

def delete(request, user_id):
    pass