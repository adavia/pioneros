#-*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget = forms.TextInput())
    email = forms.EmailField(widget = forms.TextInput())
    message_text = forms.CharField(widget = forms.Textarea())