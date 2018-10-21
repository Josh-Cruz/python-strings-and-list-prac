# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = "This is where all future blogs will go"
    return HttpResponse(response)

def new(request):
    display = "this is a placeholder for where we will make future blogs"
    return HttpResponse(display)

def create(request):
   return redirect("/")

def show(request):
    placeholder = "this is where we will store blog number {{number}}"
    return HttpResponse(placeholder)

def edit(request):
    placeholder = "this will let you edit blog {{number}}"
    return HttpResponse(placeholder)

def destroy(request):
    return redirect("/")
