#-*- coding: utf-8 -*-
from django.shortcuts import render
from teams.models import Center, Directive, Player, Game

def history(request):
    return render(request, 'teams/history.html')

def stadium(request):
    return render(request, 'teams/stadium.html')

def directive(request):
    directives = Directive.objects.filter(position__exact='directivo').order_by('id')
    return render(request, 'teams/directive.html', {
    				'directives': directives
    })

def centers(request):
    centers = Center.objects.all()
    return render(request, 'teams/centers.html', {
    				'centers': centers
    })

def team(request):
    players = Player.objects.all()
    return render(request, 'teams/team.html', {
    				'players': players
    })

def coach(request):
    players = Player.objects.all()
    return render(request, 'teams/coach.html', {
    				'players': players
    })

def positions(request):
    return render(request, 'teams/positions.html')

def games(request):
    games = Game.objects.all()[:5]
    return render(request, 'teams/games.html', {
                    'games': games
    })