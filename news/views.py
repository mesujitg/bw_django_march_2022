from django.http import HttpResponse
from django.shortcuts import render


def show_news(request):
    return HttpResponse('news')


def show_news_by_category(request, cid):
    return HttpResponse(f'category news {cid}')


def show_single_news(request, nid):
    return render(request, 'single.html')
