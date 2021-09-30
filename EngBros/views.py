from django.shortcuts import redirect, render,HttpResponse
from .models import Products
from math import ceil
# Create your views here.

def index(request):
    products = Products.objects.all
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # next lind add ( 'no_of_slides':nSlides , 'range':range (nSlides) ,)
    params ={'webname': 'Ziddi Tech', 'product': products , }
    return render(request,'index.html',params)
    

def inpage(redirect):
    return render(redirect,'inner-page.html')
def portfolio(redirect):
    return render(redirect,'portfolio-details.html')
def graphic(redirect):
    return render(redirect,'graphic.html')
def webdev(redirect):
    return render(redirect,'webdev.html')
def seo(redirect):
    return render(redirect,'seo.html')
def digitalmarketing(redirect):
    return render(redirect,'digitalmarketing.html')
