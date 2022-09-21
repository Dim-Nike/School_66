from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import DetailView

from User.models import CustomUser


def landing(req):
    data = {
        'title': '',
        'title_page': 'Ваши предметы',
        'subjects': Subject.objects.order_by('name_subjects')
    }
    if CustomUser.is_authenticated:
        print(CustomUser.is_authenticated)
        return render(req, 'lecture/landing.html', data)
    else:
        return redirect('login')


def lecture(req):
    data = {
        'title_page': 'Лекции',
        'title': 'Страница с темами лекций'
    }

    return render(req, 'lecture/details_lectures.html', data)


def detailLectureTopic(req, sub_id):
    data = {
        'lectures': Lecture.objects.filter(cat_id=sub_id).order_by('-date'),
        'title_page': 'Уроки',
        'title': 'Учебно-методические материалы'
    }

    return render(req, 'lecture/details_lectures.html', data)


class DetailLesson(DetailView):
    paginate_by = 2
    model = Lecture
    template_name = 'lecture/detail_lesson.html'
    context_object_name = 'lesson'


# def logout_user(req):
#     logout(req)
#     print(f'Я вышел с аккаунта')
#

