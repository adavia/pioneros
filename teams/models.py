import os
from django.db import models
from django.utils import timezone
from PIL import Image as PImage, ImageOps
from os.path import join as pjoin
from string import join
from tempfile import NamedTemporaryFile
from django.core.files import File
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

class Nation(models.Model):
    class Meta:
        verbose_name_plural = "nations"

    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name

class Position(models.Model):
    class Meta:
        verbose_name_plural = "positions"

    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name

class Roll(models.Model):
    class Meta:
        verbose_name_plural = "rolls"

    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name

class League(models.Model):
    class Meta:
        verbose_name_plural = "leagues"

    name = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name

class Stadium(models.Model):
    class Meta:
        verbose_name_plural = "stadiums"

    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    location = models.CharField(max_length = 150, blank = True)
    phone = models.CharField(max_length = 20, blank = True)
    contact = models.CharField(max_length = 100, blank = True)
    image = models.ImageField(upload_to = 'stadiums/', null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name

@receiver(post_delete, sender=Stadium)
def delete(sender, **kwargs):
    instance = kwargs['instance']
    instance.image.delete(save=False)

class Team(models.Model):
    class Meta:
        verbose_name_plural = "teams"

    name = models.CharField(max_length = 100)
    stadium = models.OneToOneField(Stadium)
    league = models.ManyToManyField(League)
    image = models.ImageField(upload_to = 'teams/', null = True, blank = True)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name

    def thumbnail(self):
        if self.image.name:
            return '<a href="/media/%s"><img src="/media/%s" width="50" height="50"/></a>'%(self.image.name, self.image.name)
        else:
            return '<a href="/static/images/no_image.jpg"/><img src="/static/images/no_image.jpg"/></a>'

    thumbnail.allow_tags = True

@receiver(post_delete, sender = Team)
def delete(sender, **kwargs):
    instance = kwargs['instance']
    instance.image.delete(save = False)

class Directive(models.Model):
    class Meta:
        verbose_name_plural = "directives"

    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    nickname = models.CharField(max_length = 100, blank = True)
    team = models.ForeignKey(Team)
    roll = models.ForeignKey(Roll)
    position = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 20, blank = True)
    email = models.CharField(max_length = 100, blank = True)
    description = models.TextField(max_length = 250, blank = True)
    image = models.ImageField(upload_to = 'directives/', null = True, blank = True)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "%s %s"%(self.name, self.last_name)

@receiver(post_delete, sender=Directive)
def delete(sender, **kwargs):
    instance = kwargs['instance']
    instance.image.delete(save=False)

class Center(models.Model):
    team = models.OneToOneField(Team)
    title = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

class CenterLocation(models.Model):
    center = models.ForeignKey(Center)
    name = models.CharField(max_length=50, blank=True)
    location = models.TextField()
    trainers = models.ManyToManyField(Directive)
    responsable = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name

class CenterSchedule(models.Model):
    DAYS_OF_WEEK = (
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sabado'),
        ('Domingo', 'Domingo'),
    )
    center_location = models.ForeignKey(CenterLocation)
    time_frame = models.CharField(max_length=50)
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.center_location.name

class Player(models.Model):
    class Meta:
        verbose_name_plural = "players"

    team = models.ForeignKey(Team, null = True)
    name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 150)
    nickname = models.CharField(max_length = 100, blank = True)
    nationality = models.ForeignKey(Nation, null = True, blank = True)
    birth_date = models.DateField(default=timezone.now)
    height = models.DecimalField(max_digits = 5, decimal_places = 2, null = True, blank = True)
    weight = models.IntegerField(null = True, blank = True)
    position = models.ForeignKey(Position, null = True, blank = True)
    goals = models.IntegerField(null = True, blank = True)
    image = models.ImageField(upload_to = 'players/', null = True, blank = True)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return "%s %s"%(self.name, self.last_name)

    def thumbnail(self):
        if self.image.name:
            return '<a href="/media/%s"><img src="/media/%s" width="50" height="50"/></a>'%(self.image.name, self.image.name)
        else:
            return '<a href="/static/images/no_image.jpg"/><img src="/static/images/no_image.jpg"/></a>'

    thumbnail.allow_tags = True

@receiver(post_delete, sender = Player)
def delete(sender, **kwargs):
    instance = kwargs['instance']
    instance.image.delete(save = False)

class Game(models.Model):
    class Meta:
        verbose_name_plural = "games"

    league = models.ForeignKey(League)
    local = models.ForeignKey(Team, related_name = 'local_team')
    visitor = models.ForeignKey(Team, related_name = 'visitor_team')
    date = models.DateTimeField()
    score_local = models.IntegerField(null = True, blank = True)
    score_visitor = models.IntegerField(null = True, blank = True)
    status = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return str(self.created_at)

class Image(models.Model):
    class Meta:
        verbose_name_plural = "images"
        ordering = ["created_at"]

    title = models.CharField(max_length=60, blank=True)
    game = models.ForeignKey(Game)
    description = models.TextField(max_length=200, blank=True)
    image = models.ImageField(upload_to='games/')
    thumbnail1 = models.ImageField(upload_to='games/thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return unicode(self.image.name)

    def save(self, *args, **kwargs): #Guardamos las dimensiones de la imagen
        super(Image, self).save(*args, **kwargs)
        img = PImage.open(pjoin(settings.MEDIA_ROOT, self.image.name))
        self.width, self.height = img.size
        self.crop(img, 1, (400,400))
        super(Image, self).save(*args, **kwargs)

    def crop(self, img, num, size):
        fn, ext = os.path.splitext(self.image.name)
        imagecrop = ImageOps.fit(img, size, PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb" + str(num) + ext
        tf = NamedTemporaryFile()
        imagecrop.save(tf.name, "JPEG")
        thumbnail = getattr(self, "thumbnail%s" % num)
        thumbnail.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()

    def thumbnail(self):
        if self.image.name:
            return '<a href="/media/%s"><img src="/media/%s" width="50" height="50"/></a>'%(self.image.name, self.image.name)
        else:
            return '<a href="/static/images/no_image.jpg"/><img src="/static/images/no_image.jpg"/></a>'

    thumbnail.allow_tags = True

@receiver(post_delete, sender=Image)
def delete(sender, **kwargs):
    instance = kwargs['instance']
    instance.image.delete(save= False)
    instance.thumbnail.delete(save=False)

