from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    chars=list("abcdefghijklmnopqrstuvwxyz")
    length=int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        chars.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('special'):
        chars.extend(list("!@#$%^&*()_+"))
    if request.GET.get('numbers'):
        chars.extend(list("1234567890"))
    thepassword=''
    print(chars)
    for x in range(length):
        thepassword+=random.choice(chars)
    return render(request,'generator/password.html',{'password':thepassword})
