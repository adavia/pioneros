# -*- coding: utf-8 -*-
from django.db import models
from users.models import User
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver

def url(self, filename):
    path = 'users/%s/%s'%(self.user.username, filename)
    return path

class Profile(models.Model):
    user = models.OneToOneField(User)
    birth_date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=url, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.user.username

@receiver(post_delete, sender=Profile)
def delete(sender, **kwargs):
    instance = kwargs['instance']
    instance.image.delete(save=False)

User.profile = property(lambda u: Profile.objects.get_or_create(user = u) [0])
