from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

def homepage(request):
    with open('articles.json', encoding='utf-8') as f:
        articles = json.load(f)


    return render(request, 'content/homepage.html', {'articles': articles})

def article(request, id):
    with open('articles.json', encoding='utf-8') as f:
        articles = json.load(f)

    article = articles[id]
    return render(request, 'content/article.html', {'article': article})

def article_context(request, war):
    with open('articles.json', encoding='utf-8') as f:
        articles = json.load(f)

    war_articles = [article for article in articles if war in article['tags']]
    return render(request, 'content/article_context.html', {'war_articles': war_articles})
