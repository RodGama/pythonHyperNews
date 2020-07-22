from datetime import datetime, timedelta
import json

from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from hypernews.settings import NEWS_JSON_PATH

with open(NEWS_JSON_PATH, 'r') as json_file:
    news_list = json.load(json_file)


def retorna_data(e):
    return e['created']


def retorna_id(e):
    return e['link']


news_list.sort(reverse=True, key=retorna_id)
max_link = news_list[0]
news_list.sort(reverse=True, key=retorna_data)


# Create your templates here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        return redirect('news/')
       # return render(request, 'home.html')


class NewsPage(View):
    def get(self, request, news_id, *args, **kwargs):
        new_page = None
        for i in news_list:
            if news_id == i['link']:
                new_page = i
        context = {
            'news': new_page
        }
        if new_page is None:
            raise Http404
        return render(request, 'news.html', context)


class NewsHomePage(View):
    def get(self, request, *args, **kwargs):
        context = {
            'news_list': news_list,
        }
        search = request.GET.get('q', '')
        if search != '':
            new_page = []
            for i in news_list:
                print(i["text"].find(search), i["text"],search)
                if i["text"].find(search) != -1:
                    new_page.append(i)
            context = {
                'news_list': new_page
            }
        return render(request, 'newshome.html', context)


class NewsCreatePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'createnews.html')

    def post(self, request, *args, **kwargs):
        global news_list
        title = request.POST.get('title')
        text = request.POST.get('text')
        created = str(datetime.today())
        link_id = max_link['link'] + 1
        news = {"created": created, "text": text, "title": title, "link": link_id}
        news_list.append(news)
        lista_final = json.dumps(news_list)
        print(type(lista_final))
        with open(NEWS_JSON_PATH, 'w') as j:
            j.write(lista_final)

        return redirect("/news/")
