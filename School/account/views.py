from django.shortcuts import render, redirect
from django.core.mail import send_mail
# Create your views here.
from User.models import CustomUser
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
    send_mail_msg = send_mail(f'Вас привествует, 14 школа!',
                              f'Добрый день {person[0].password}\n',
                              'officialtriggermobile@gmail.com',
                              ['nikitin_dima2000dn@mail.ru'], fail_silently=False)
    for person in persons:
        print(f'Имя: {person.username}')

    send_msg_mail = ''

    for person in persons:
        send_msg_mail = send_mail(f'Вас привествует, 14 школа!',
                                  f'Добрый день, {person.last_name} {person.first_name}\n'
                                  f'Ваш логин: {person.username}\n'
                                  f'Ваш класс: {person.catClassUser}\n'
                                  f'Ваш пароль: {person.password}',
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