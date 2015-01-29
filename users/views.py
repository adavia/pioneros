#-*- coding: utf-8 -*-
from django.http import Http404, HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import (
    login as login_view,
    logout as logout_view,
    password_reset as password_reset_view,
    password_reset_done as password_reset_done_view,
    password_reset_confirm as password_reset_confirm_view,
    password_reset_complete as password_reset_complete_view
)

from users.models import User
from users.forms import SignupForm, LoginForm, ValidationOnForgotPasswordForm
from users.utils import default_token_generator

def user_signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        message = ''
        if request.method == 'POST':
            f = SignupForm(request.POST)
            if f.is_valid():
                user = f.save()

                user = authenticate(email = f.cleaned_data['email'], password = f.cleaned_data['password'])
                #login(request, user)

                user.send_verification_mail(request)

                message = """Un email de confirmación fué enviado al correo proporcionado. 
                    Muchas gracias.."""
        else:
            f = SignupForm()

        return render(request, 'users/user_signup.html', {
            'form': f,
            'message':message
        })

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        message = ''
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/')
                    else:
                        message = """Su cuenta no se encuentra activada. Por favor verifique su correo. 
                            Muchas gracias.."""
                else:
                    message = """Usuario y/o Contraseña incorrectos. Verifique nuevamente los datos ingresados.
                        Muchas Gracias.."""
        else:
            form = LoginForm()
        return render(request, 'users/user_login.html', {
            'form':form, 
            'message':message
        })


def user_logout(request):
    return logout_view(request, next_page='/')

@login_required
def user_verification(request):
    if request.method == 'POST':
        request.user.send_verification_mail(request)

    return render(request, 'users/user_verification.html')

def user_verify(request, uid, token):
    try:
        uid = urlsafe_base64_decode(uid)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError):
        raise Http404

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()

        return redirect('/ingresar')
    else:
        raise Http404

def user_password_reset(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return password_reset_view(
            request,
            template_name='users/user_password_reset.html',
            email_template_name='users/user_password_reset_email.txt',
            subject_template_name='users/user_password_reset_subject.txt',
            password_reset_form=ValidationOnForgotPasswordForm,
            post_reset_redirect=reverse('user:password_reset_done')
        )

def user_password_reset_done(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return password_reset_done_view(
            request,
            template_name='users/user_password_reset_done.html'
        )

def user_password_reset_confirm(request, uidb64, token):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return password_reset_confirm_view(
            request,
            template_name='users/user_password_reset_confirm.html',
            uidb64=uidb64,
            token=token,
            post_reset_redirect=reverse('user:password_reset_complete')
        )

def user_password_reset_complete(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return password_reset_complete_view(
            request,
            template_name='users/user_password_reset_complete.html'
        )
