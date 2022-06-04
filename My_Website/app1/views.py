from django import http
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.


def home_fun(request):
    return render(request, 'home.html')


def about_fun(request):
    return render(request, 'about.html')


def profile_fun(request):
    return render(request, 'profile.html')


def contact_fun(request):
    #form = ContactForm()
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
            form = ContactForm()
    return render(request,'contact.html',{'forms':form})

def gallery_fun(request):
    return render(request, 'base.html')
