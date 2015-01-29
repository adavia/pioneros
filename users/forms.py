#-*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordResetForm
from users.models import User

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget = forms.PasswordInput())
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'confirm_password')
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        m = super(SignupForm, self).save(commit=False)
        m.set_password(self.cleaned_data.get('password'))

        if commit:
            m.save()

        return m

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username = username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('El usuario ya existe en nuestros registros')

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            u = User.objects.get(email = email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('El email ya existe en nuestros registros')

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password == confirm_password:
            pass
        else:
            raise forms.ValidationError('Las contraseñas no coinciden')

class LoginForm(forms.Form):
    email = forms.EmailField(widget = forms.TextInput())
    password = forms.CharField(widget = forms.PasswordInput())

class ValidationOnForgotPasswordForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError('No existe ningún usuario registrado con este email!')

        return email
