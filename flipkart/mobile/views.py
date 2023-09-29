from django.shortcuts import render

# Create your views here.
def realme(request): 
    return render(request,"realme.html") 
def redme(request): 
    return render(request,"redme.html") 
def nokia(request): 
    return render(request,"nokia.html")