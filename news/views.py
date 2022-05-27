from django.http import HttpResponse
from django.shortcuts import render

from broadway.settings import MEDIA_URL
from news.models import News


def show_news(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})


def show_news_by_category(request, cid):
    news = News.objects.filter(category_id=cid)
    return render(request, 'news.html', {'news': news})


def show_single_news(request, nid):
    # news = News.objects.filter(id=nid) #returns list of object/s
    news = News.objects.get(id=nid) #returns object
    return render(request, 'single.html', {'news': news})
