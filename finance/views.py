from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm

def index(request):
    return render(request, 'finance/index.html')

def blog(request):
    return render(request, 'finance/blog.html')

def services(request):
    return render(request, 'finance/services.html')

def contact(request):
    return render(request, 'finance/contact.html')

def about(request):
    return render(request, 'finance/about.html')

def login(request):
    return render(request, 'finance/login.html')

def register(request):
    if request == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Redirect after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'finance/register.html', {'form': form})
