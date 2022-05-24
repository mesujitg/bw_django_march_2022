from django.http import HttpResponse
from django.shortcuts import render
from categories.models import Category
from news.models import News

# https: // www.codegrepper.com / code - examples / python / frameworks / flask / merge + two + query + sets + django


def show_home(request):
    # flash_news = News.objects.filter(category_id=2).order_by('-id')[:4]
    flash_news = News.objects.filter(category__title='Business').order_by('-id')[:4]
    return render(request, 'index.html', {'flash_news': flash_news})


def show_about(request):
    return render(request, 'about.html')


def show_contacts(request):
    return render(request, 'contacts.html')

