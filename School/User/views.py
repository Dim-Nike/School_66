from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView

from .forms import CustomUserCreationForm
from .models import CustomUser


# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'User/login.html'
#
#     def test(self, req):
#         if req.method == 'POST':
#             return self.form_class
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Авторизация пользователя'
#         context['page_title'] = 'Авторизация'
#         return context
#
#     def get_success_url(self):
#         return reverse_lazy('landing')


def loginUser(req):
    auth = AuthenticationForm
    data = {'title': 'Авторизация',
            'title_page': 'Авторизация',
            'form': auth}
    if req.method == 'POST':
        auth_user = authenticate(username=req.POST["username"],
                                 password=req.POST["password"])

        if auth_user is not None:
            login(req, auth_user)

            return redirect('landing')
        # else:
        #     # print(f'Ошибка аундификации. Пользователя {req.POST.send["username"]} не существует!')
    return render(req, 'User/login.html', data)


class RegisterUser(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'User/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        context['page_title'] = 'Регистрация'
        return context

    def post(self, req, *args, **kwargs):
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('login')
        else:
            return render(req, self.template_name, {'form': form})