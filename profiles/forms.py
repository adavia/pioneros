#-*- coding: utf-8 -*-
from django import forms
from profiles.models import Profile

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birth_date', 'location', 'description', 'image')