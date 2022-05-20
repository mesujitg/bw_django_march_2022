from django.http import HttpResponse
from django.shortcuts import render
from categories.models import Category
from news.models import News


# https: // www.codegrepper.com / code - examples / python / frameworks / flask / merge + two + query + sets + django


def show_home(request):
    categories = Category.objects.all()
    # flash_news = News.objects.filter(category_id=2).order_by('-id')[:4]
    flash_news = News.objects.filter(category__title='Something').order_by('-id')[:4]
    return render(request, 'index.html', {'categories': categories,
                                          'flash_news': flash_news})


def show_about(request):
    return render(request, 'base.html')


def show_contacts(request):
    return HttpResponse('Contacts')

