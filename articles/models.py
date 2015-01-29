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

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=200)
    url = models.SlugField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    class Meta:
        verbose_name_plural = "articles"

    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150, blank=True)
    body = models.TextField()
    aside = models.TextField(blank=True)
    url = models.SlugField(max_length=200)
    category = models.ForeignKey(Category)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.title

    def images(self):
        lst = [x.image.name for x in self.image_set.all()]
        lst = ["<a href='/media/%s'>%s</a>" % (x, x.split('/')[-1]) for x in lst]
        return join(lst, ', ')

    images.allow_tags = True

    def videos(self):
        text = ""
        for i in self.video_set.all():
            text = text + '<br />' + str(i.title)
        return text

    videos.allow_tags = True

class Image(models.Model):
    class Meta:
        verbose_name_plural = "images"
        ordering = ["created_at"]

    title = models.CharField(max_length=60, blank=True)
    article = models.ForeignKey(Article)
    description = models.TextField(max_length=200, blank=True)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/')
    thumbnail1 = models.ImageField(upload_to='uploads/thumbnails1/', blank=True, null=True)
    thumbnail2 = models.ImageField(upload_to='uploads/thumbnails2/', blank=True, null=True)
    thumbnail3 = models.ImageField(upload_to='uploads/thumbnails3/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return unicode(self.image.name)

    def save(self, *args, **kwargs): #Guardamos las dimensiones de la imagen
        super(Image, self).save(*args, **kwargs)
        img = PImage.open(pjoin(settings.MEDIA_ROOT, self.image.name))
        self.width, self.height = img.size
        self.resize(img, 1, (1024,350))
        self.resize(img, 2, (900,400))
        self.crop(img, 3, (400,400))
        super(Image, self).save(*args, **kwargs)

    def resize(self, img, num, size):
        fn, ext = os.path.splitext(self.image.name)
        imageresize = img.resize(size, PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb" + str(num) + ext
        tf = NamedTemporaryFile()
        imageresize.save(tf.name, "JPEG")
        thumbnail = getattr(self, "thumbnail%s" % num)
        thumbnail.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()

    def crop(self, img, num, size):
        fn, ext = os.path.splitext(self.image.name)
        imagecrop = ImageOps.fit(img, size, PImage.ANTIALIAS)
        thumb_fn = fn + "-thumb" + str(num) + ext
        tf = NamedTemporaryFile()
        imagecrop.save(tf.name, "JPEG")
        thumbnail = getattr(self, "thumbnail%s" % num)
        thumbnail.save(thumb_fn, File(open(tf.name)), save=False)
        tf.close()

    """
    Funciona en modelos m2m
    def imgproperty_(self):
        lst = [x[1] for x in self.imgproperty.values_list()]
        return str(join(lst, ', '))
    """

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
    instance.thumbnail1.delete(save=False)
    instance.thumbnail2.delete(save=False)
    instance.thumbnail3.delete(save=False)

class Video(models.Model):
    class Meta:
        verbose_name_plural = "videos"
        ordering = ["created_at"]

    title = models.CharField(max_length=100, blank=True)
    article = models.ForeignKey(Article)
    url = models.SlugField(max_length=200)
    link = models.CharField(max_length=200, blank=True)
    description = models.TextField(max_length=400, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return unicode(self.title)

class Sponsor(models.Model):
    class Meta:
        verbose_name_plural = "sponsors"

    name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=200, blank=True)
    url = models.SlugField(max_length=200)
    link = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to = 'sponsors/', null = True, blank = True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return unicode(self.name)

@receiver(post_delete, sender=Sponsor)
def delete(sender, **kwargs):
    instance = kwargs['instance']
    instance.image.delete(save= False)
