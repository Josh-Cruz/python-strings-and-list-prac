from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "landing_page/index.html", context)
