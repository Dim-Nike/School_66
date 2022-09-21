from django.shortcuts import render
from . import models
from django.views.generic import DetailView


def title_news(req):
    data = {
        'title_page': 'Уведомления',
        'title': 'Новости',
        'news': models.News.objects.order_by('-date')
    }
    return render(req, 'news/index.html', data)


class DetailNews(DetailView):
    model = models.News
    template_name = 'news/detail_news.html'
    context_object_name = 'detail_news'