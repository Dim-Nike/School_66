from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.
from User.models import CustomUser
from lecture.models import TestResult
from django.contrib.auth import get_user_model


def render_user(req):
    data = {
        'title_page': 'Аккаунт',
        'title': '',
        'users': CustomUser
    }

    return render(req, 'account/index.html', data)


def send_msg(req):
    person = CustomUser.objects.order_by('catClassUser')
    users = get_user_model()
    persons = users.objects.all()
    test_result = TestResult.objects.order_by('test')

    # for show in test_result:
    #
    #     print(f'Test - {show.test}\n'
    #           f'User - {show.user}\n'
    #           f'Date - {show.date}\n'
    #           f'Result test - {show.result_test}\n\n')

    # for person in persons:
    #     print(f'Имя: {person.username}')

    send_msg_mail = ''


    # for person in persons:
    #     for show in test_result:
    #         if person.first_name + " " + person.last_name == show.user:
    #             result += f'Наименование теста - {show.test}\nПользователь - {show.user}\nДата прохождения теста - {show.date}\nКоличество баллов - {show.result_test}\n\n'

    for person in persons:
        result = ''
        for person in persons:
            for show in test_result:
                if person.first_name + " " + person.last_name == show.user:
                    result += f'Наименование теста - {show.test}\nПользователь - {show.user}\nДата прохождения теста - {show.date}\nКоличество баллов - {show.result_test}\n\n'

        send_msg_mail = send_mail(f'Вас привествует, 14 школа!',
                                  f'Добрый день, {person.last_name} {person.first_name}\n'
                                  f'Ваш логин: {person.username}\n'
                                  f'Ваш класс: {person.catClassUser}\n'
                                  f'Информация о тестах\n\n{result}',
                                  'officialtriggermobile@gmail.com',
                                  [person.email], fail_silently=False)
    if send_msg_mail:
        print('Письмо отправилось успешно!')
        return redirect('landing')
    else:
        print('Письмо не отправилось!')


def notify_mail(req):
    users = get_user_model()
    persons = users.objects.all()
    send_notify = ''
    list_result_test = []

    for person in persons:
        send_notify = send_mail(f'Вас привествует, 14 школа!',
                                  'Уведомляем вас о тестах',
                                  'officialtriggermobile@gmail.com',
                                  [person.email], fail_silently=False)
    if send_notify:
        print('Письмо отправилось успешно!')
        return redirect('landing')
    else:
        print('Письмо не отправилось!')