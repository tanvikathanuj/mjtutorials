#from django.shortcuts import HTTPResponse
from django.shortcuts import render
from django.shortcuts import redirect

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def our_services(request):
    return render(request, 'our_services.html')

def facebook(request):
    return render(request,'facebook.html')

def twitter(request):
    return render(request,'twitter.html')

def instagram(request):
    return render(request,'instagram.html')

def linkedin(request):
    return render(request,'linkedin.html')

def email(request):
    return render(request,'email.html')

def courses(request):
    return render(request,'courses.html')

def ComCourse(request):
    return render(request,'ComCourse.html')

def ScCourse(request):
    return render(request,'ScCourse.html')

def payment(request):
    return render(request,'pay.html')
