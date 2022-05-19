from django.http import HttpResponse
from django.shortcuts import render
from categories.models import Category


def show_home(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})


def show_about(request):
    return render(request, 'test.html')


def show_contacts(request):
    return HttpResponse('Contacts')

