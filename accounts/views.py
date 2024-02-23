# from django.shortcuts import render, redirect
# from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from contacts.models import Contact
# from listings.models import Listing
from typing import Union

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser

from modules.services.mixins import UserIsNotAuthenticated
from our_company.models import OurCompany
from django.views.generic import CreateView, View, TemplateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.core import serializers
import json
from django.forms.models import model_to_dict
from django.shortcuts import redirect
from rest_framework import generics, status
from rest_framework.response import Response
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Profile

from .forms import (UserUpdateForm, ProfileUpdateForm, UserRegisterForm, UserLoginForm,
                    UserPasswordChangeForm, UserForgotPasswordForm, UserSetNewPasswordForm)

User = get_user_model()


class UserProfileAPIView(generics.GenericAPIView):
    model = User

    def get(self, request):
        user = auth.get_user(request)
        if not isinstance(user, AnonymousUser):
            return Response(
                {"result": 'success',
                 'id': user.id,
                 'username': user.username,
                 'first_name': user.first_name,
                 'last_name': user.last_name,
                 'email': user.email,
                 'message': 'Current user data'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"result": 'error',
                 'message': 'User is not authenticated'},
                status=status.HTTP_401_UNAUTHORIZED
            )


class ProfileDetailView(DetailView):
    """
    Представление для просмотра профиля
    """
    model = Profile
    context_object_name = 'profile'
    template_name = 'includes/content/lk.html'
    queryset = model.objects.all().select_related('user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Страница пользователя: {self.object.user.username}'
        context['our_company'] = OurCompany.objects.all().first()
        return context


class ProfileUpdateView(UpdateView):
    """
    Представление для редактирования профиля
    """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_edit.html'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Редактирование профиля пользователя: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        context['our_company'] = OurCompany.objects.all().first()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super(ProfileUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'slug': self.object.slug})


class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Авторизация на сайте
    """
    form_class = UserLoginForm
    template_name = 'accounts/registration/user_login.html'
    next_page = 'index'
    success_message = 'Добро пожаловать на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация на сайте'
        context['our_company'] = OurCompany.objects.all().first()
        return context


class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    Изменение пароля пользователя
    """
    form_class = UserPasswordChangeForm
    template_name = 'accounts/registration/user_password_change.html'
    success_message = 'Ваш пароль был успешно изменён!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пароля на сайте'
        context['our_company'] = OurCompany.objects.all().first()
        return context

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'slug': self.request.user.profile.slug})


class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'accounts/registration/user_password_reset.html'
    success_url = reverse_lazy('index')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'accounts/email/password_subject_reset_mail.txt'
    email_template_name = 'accounts/email/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        context['our_company'] = OurCompany.objects.all().first()
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    Представление установки нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'accounts/registration/user_password_set_new.html'
    success_url = reverse_lazy('index')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        context['our_company'] = OurCompany.objects.all().first()
        return context


class UserRegisterView(UserIsNotAuthenticated, CreateView):
    """
    Представление регистрации на сайте с формой регистрации
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/registration/user_register.html'
    success_message = 'Вы успешно зарегистрировались. Можете войти на сайт!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация на сайте'
        context['our_company'] = OurCompany.objects.all().first()
        return context

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        # Функционал для отправки письма и генерации токена
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        activation_url = reverse_lazy('confirm_email', kwargs={'uidb64': uid, 'token': token})
        current_site = Site.objects.get_current().domain
        send_mail(
            'Подтвердите свой электронный адрес',
            f'Пожалуйста, перейдите по следующей ссылке, чтобы подтвердить свой адрес электронной почты: http://{current_site}{activation_url}',
            'service.notehunter@gmail.com',
            [user.email],
            fail_silently=False,
        )
        return redirect('email_confirmation_sent')


class UserConfirmEmailView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64)
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('email_confirmed')
        else:
            return redirect('email_confirmation_failed')


class EmailConfirmationSentView(TemplateView):
    template_name = 'accounts/registration/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        context['our_company'] = OurCompany.objects.all().first()
        return context


class EmailConfirmedView(TemplateView):
    template_name = 'accounts/registration/email_confirmed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес активирован'
        context['our_company'] = OurCompany.objects.all().first()
        return context


class EmailConfirmationFailedView(TemplateView):
    template_name = 'accounts/registration/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес не активирован'
        context['our_company'] = OurCompany.objects.all().first()
        return context


def logout_view(request):
    logout(request)
    return redirect('index') # на главную страницу сайта

# class UserLogoutView(LogoutView):
#     """
#     Выход с сайта
#     """
#     print('logout')
#     next_page = 'index'


# def register(request):
#     if request.method == 'POST':
#         # Get form values
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#
#         # Check if passwords match
#         if password == password2:
#             # Check username
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'That username is taken')
#                 return redirect('register')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, 'That email is being used')
#                     return redirect('register')
#                 else:
#                     # Looks good
#                     user = User.objects.create_user(username=username, password=password, email=email,
#                                                     first_name=first_name, last_name=last_name)
#                     # Login after register
#                     # auth.login(request, user)
#                     # messages.success(request, 'You are now logged in')
#                     # return redirect('index')
#                     user.save()
#                     messages.success(request, 'You are now registered and can log in')
#                     return redirect('login')
#         else:
#             messages.error(request, 'Passwords do not match')
#             return redirect('register')
#     else:
#         return render(request, 'accounts/register.html')
#
#
# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             auth.login(request, user)
#             messages.success(request, 'You are now logged in')
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid credentials')
#             return redirect('login')
#     else:
#         return render(request, 'accounts/login.html')
#
#
# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         messages.success(request, 'You are now logged out')
#         return redirect('index')
#
#
# def dashboard(request):
#     user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
#     listings = Listing.objects.order_by('-list_date').filter(is_published=True, offer_type='rent')
#     our_company = OurCompany.objects.all().first()
#
#     context = {
#         'our_company': our_company,
#         'listings': listings,
#         'contacts': user_contacts
#     }
#     return render(request, 'accounts/dashboard.html', context)
