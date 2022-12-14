import random
import threading
from asyncio import sleep

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import DetailView
import datetime
from User.models import CustomUser

id_test = 0
start_time_test = 0


def landing(req):
    data = {
        'title': 'Предметы',
        'title_page': 'Главная страница',
        'subjects': Subject.objects.order_by('name_subjects')
    }
    if CustomUser.is_authenticated:
        return render(req, 'lecture/landing.html', data)
    else:
        return redirect('login')


def lecture(req):
    data = {
        'title_page': 'Темы лекций',
        'title': 'Лекции'
    }

    return render(req, 'lecture/details_lectures.html', data)


def detailLectureTopic(req, sub_id):
    data = {
        'lectures': Lecture.objects.filter(cat_id=sub_id).order_by('-date'),
        'test_result': TestResult.objects.order_by('date'),
        'title_page': 'Уроки',
        'title': 'Учебно-методические материалы'
    }

    return render(req, 'lecture/details_lectures.html', data)


class DetailLesson(DetailView):
    paginate_by = 2
    model = Lecture
    template_name = 'lecture/detail_lesson.html'
    context_object_name = 'lesson'


def detailLesson(req, sub_id):
    lecture_material = Lecture.objects.filter(id=sub_id).order_by('date')
    test_result = TestResult.objects.order_by('date')
    count_attempt = lecture_material[0].test.attempts

    for result in test_result:
        if result.test == lecture_material[0].test.name_test:
            user = req.user.first_name + ' ' + req.user.last_name
            if result.user == user:
                count_attempt -= 1

    now_time = datetime.datetime.now()
    print(f'{type(now_time)}||{type(lecture_material[0].test.end_date)}')
    if now_time.timestamp() > lecture_material[0].test.end_date.timestamp():
        print('Время теста истекло!')
    else:
        print('Пройти тест')

    data = {
        'title_page': 'Тема урока',
        'title': 'Урок',
        'lessons': Lecture.objects.filter(id=sub_id).order_by('date'),
        'count_attempt': count_attempt,
        'now_time': now_time.timestamp(),
        'test_time': lecture_material[0].test.end_date.timestamp(),

    }

    return render(req, 'lecture/detail_lesson.html', data)


def show_test(req, sub_id):
    global id_test
    global start_time_test
    time_minute_test = 0

    now_time = str(datetime.datetime.now())
    id_test = sub_id
    test = Test.objects.filter(id=sub_id).order_by('start_date')
    time_minute_test = test[0].distance
    now_time_int = int(now_time[14] + now_time[15])
    test_dict = {}
    answer_list = []



    # for i_answer, el_answer in enumerate(test[0].answer.all()):
    #     ask_list = []
    #     if i_answer + 1 > test[0].count_answer:
    #         print(i_answer)
    #         break
    #     answer_list.append(el_answer)
    #     for i_ask, el_ask in enumerate(el_answer.ask.all()):
    #         if i_ask + 1 > el_answer.count_ask:
    #             print(i_ask)
    #             break
    #         ask_list.append(el_ask)
    #     answer_dict[el_answer] = ask_list

    for el_answer in enumerate(test[0].answer.all()):
        answer_list.append(el_answer)
    random_answer_list = random.sample(answer_list, test[0].count_answer)
    for el_answer in random_answer_list:
        ask_list = []
        for el_ask in el_answer[1].ask.all():
            ask_list.append(el_ask)

        ask_list = random.sample(ask_list, el_answer[1].count_ask)
        test_dict[el_answer] = ask_list

    print(test_dict)


    # print(answer_dict)
    # print(answer_list)
    # print(ask_list)

    # print(answer_list[0])

    # def check_time_test(time_test, time_minute_test):
    #     time_minute_test -= 1
    #     print(time_minute_test)
    #     if time_minute_test <= 0:
    #         print('Время вышло')
    #         return 0
    #     if not time_test.is_set():
    #         threading.Timer(1, check_time_test, [time_test, time_minute_test]).start()
    #
    # time_test = threading.Event()
    #
    # show = check_time_test(time_test=time_test, time_minute_test=time_minute_test)

    data = {
        'test': Test.objects.filter(id=sub_id).order_by('start_date'),
        'title_page': 'Тест',
        'title': 'Тест'
    }

    return render(req, 'lecture/test.html', data)


def show_result_test(req):
    global id_test
    now_data = datetime.datetime.now()
    now_data_str = str(now_data)
    req_dict = {}
    count_mark_test = 0
    test = Test.objects.filter(id=id_test).order_by('start_date')

    print(f'Now data - {now_data}')

    if req.method == 'POST':
        val = req.POST.getlist("list")

        for el in val:
            answer = el.partition("||")[0]
            ask = el[el.find('||') + 2:]
            req_dict[answer] = ask

        for el in test:
            for test_answer in el.answer.all():
                for test_ask in test_answer.ask.all():
                    test_answer_str = str(test_answer)
                    test_ask_str = str(test_ask)
                    if req_dict[test_answer_str] == test_ask_str:
                        if test_ask.ask_true:
                            count_mark_test += test_answer.mark
        #
        user = req.user.first_name + ' ' + req.user.last_name
        user_class = req.user.catClassUser
        user_class_str = str(user_class)
        user_class_int = int(user_class_str)
        test_name = Test.objects.filter(id=id_test)[0]

        result_test = TestResult()
        result_test.test = test_name
        result_test.user = user
        result_test.class_user = user_class_int
        result_test.date = str(now_data_str.partition(".")[0])
        result_test.date_user = '4321'
        result_test.result_test = count_mark_test
        result_test.save()
        # print(result_test)

        data = {
            'title': 'Результат теста',
            'result_test': result_test
        }

    return render(req, 'lecture/resultTest.html', data)

# def save_ask(req):


# def logout_user(req):
#     logout(req)
#     print(f'Я вышел с аккаунта')
#
