from django.shortcuts import render
from newsapi import NewsApiClient


# Create your views here.


def index(request):
    newsApi = NewsApiClient(api_key='c696a6e48c0a43aabb4288ce9e3ea804')
    headLines = newsApi.get_top_headlines(sources = 'the-verge,google-news')
    articles = headLines['articles']
    desc = []
    news = []
    image = []
    
    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        image.append(article['urlToImage'])
    
    mylist = zip(news, desc, image)
    
    return render(request, 'news/index.html', context = {'mylist' : mylist})

def calculator(request):
    return render(request, 'news/calculator.html')