from django.contrib import admin
from teams.models import Nation, Position, League, Team, Player, Game, Roll, Directive, Stadium, Center, CenterLocation, CenterSchedule, Image

class CenterLocationInline(admin.TabularInline):
    model = CenterLocation
    extra = 5
    exclude = ['description', 'created_at', 'updated_at']

class CenterScheduleInline(admin.TabularInline):
    model = CenterSchedule
    extra = 5
    exclude = ['created_at', 'updated_at']

class DirectiveInline(admin.TabularInline):
    model = Directive
    extra = 5
    exclude = ['phone', 'email', 'description', 'image', 'status', 'created_at', 'updated_at']

class ImageInline(admin.TabularInline):
    model = Image
    extra = 5
    include = ['image', 'title', 'description']
    exclude = ['thumbnail1', 'created_at', 'updated_at']

class CenterAdmin(admin.ModelAdmin):
    inlines = [CenterLocationInline]

class CenterLocationAdmin(admin.ModelAdmin):
    inlines = [CenterScheduleInline]

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('team', '__unicode__', 'position', 'thumbnail')
    list_filter = ('team', 'nationality', 'position')
    search_fields = ['name', 'last_name', 'nickname']
    #asi se va cambiando el orden de los campos en el admin
    fieldsets = [
        (None, {'fields': ['team', 'name', 'last_name', 'nickname', 'nationality', 'birth_date']}),
        ('Informacion adicional', {'fields': [('position', 'height', 'weight', 'goals'), 'image', 'updated_at', 'status']}),
    ]

class TeamAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'stadium', 'thumbnail']
    search_fields = ['name', 'stadium']
    inlines = [DirectiveInline]

class GameAdmin(admin.ModelAdmin):
    list_display = ['date', 'local', 'score_local', 'score_visitor', 'visitor']
    list_filter = ['local', 'league']
    search_fields = ['local']
    fieldsets = [
        (None, {'fields': ['date', 'league']}),
        ('Game', {'fields': [('local', 'score_local', 'score_visitor', 'visitor'), 'updated_at', 'status']}),
    ]
    inlines = [ImageInline]

class DirectiveAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'last_name', 'roll']
    list_filter = ['roll']
    search_fields = ['name', 'last_name', 'nickname']

admin.site.register(Nation)
admin.site.register(Position)
admin.site.register(League)
admin.site.register(Image)
admin.site.register(Roll)
admin.site.register(Stadium)
admin.site.register(Directive, DirectiveAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(CenterLocation, CenterLocationAdmin)
admin.site.register(CenterSchedule)



