from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

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
