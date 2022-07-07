from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'page/index.html')

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    generarted_password = ''
    
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    if request.GET.get('length'):
        length = int(request.GET.get('length'))
    else:
        length = 8
       
    for x in range(length):
        generarted_password += random.choice(characters)
        
    
    return render(request, 'page/password.html',{'password': generarted_password})


