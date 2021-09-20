from django.shortcuts import redirect, render,HttpResponse

# Create your views here.

def index(request):
    params ={'webname': 'Ziddi Tech',}
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
