from django.contrib import auth, messages
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import User
from news.models import News


def register(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        un = request.POST['un']
        # password = request.POST['password']
        password = make_password(request.POST['password'])

        usr = User(first_name=fn, last_name=ln, email=email, mobile=mobile,
                   address=address, username=un, password=password)
        # usr = User.objects.get(id=1)
        # usr.first_name = 'asdfas'
        usr.save()
        return redirect('home')
    else:
        return HttpResponse('Invalid access')


def user_login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']

        user = auth.authenticate(username=un, password=pw)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            messages.error(request, 'Wrong Credentials')
            return redirect('home')
    else:
        return HttpResponse('Invalid access')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out')
    return redirect('home')


def user_profile(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if not password == cpassword:
            return messages.error(request, 'Password mismatch')

        if not (request.POST['password'] == request.user.password):
            password = make_password(request.POST['password'])

        user = User.objects.get(id=request.user.id)
        user.first_name = fn
        user.last_name = ln
        user.email = email
        user.mobile = mobile
        user.address = address
        user.password = password
        user.save()

        return redirect('home')

    # news = News.objects.get(id=1)
    # return render(request, 'profile.html', {'news': news})
    return render(request, 'profile.html')
