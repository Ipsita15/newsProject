from django.shortcuts import render


# Create your views here.
def home(request):
    import requests
    import json

    news_api_request = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2022-04-19&sortBy=publishedAt&apiKey=f85042a1bb054587aa9e0babd246dfc8")
    api = json.loads(news_api_request.content)
    return render(request,'home.html',{'api':api})
