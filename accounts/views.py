from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import User


def register(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        un = request.POST['un']
        pwd = request.POST['pwd']

        usr = User(first_name=fn, last_name=ln, email=email, mobile=mobile,
                   address=address, username=un, password=pwd)
        # usr = User.objects.get(id=1)
        # usr.first_name = 'asdfas'
        usr.save()
        return redirect('home')
    else:
        return HttpResponse('Invalid access')


def login(request):
    pass
