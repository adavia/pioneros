#-*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from profiles.models import Profile
from profiles.forms import EditProfileForm
from django.shortcuts import render

@login_required
def profile(request):
    message = ''
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            message = """Los datos de su perfil han sido editados correctamente"""
    else:
        user = request.user
        profile = user.profile #Con esta linea me trae el lambda definido en el modelo
        form = EditProfileForm(instance = profile)
    return render(request, 'profiles/edit.html', {
        'form':form, 
        'message':message
    })
