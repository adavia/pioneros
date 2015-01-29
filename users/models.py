from django.db import models
from django.utils.timezone import now
from django.utils.crypto import salted_hmac
from django.core.urlresolvers import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from users.utils import send_template_mail, default_token_generator

class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email), 
            last_login=now(), 
            date_joined=now(),
            is_active=False, 
            is_staff=False, 
            is_superuser=False,
            **kwargs
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(
            email=email,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            **kwargs
        )
        user.set_password(password)
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, blank=False)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def send_verification_mail(self, request):
        if not self.pk:
            self.save()

        return send_template_mail(
            'Verificacion de email',
            'users/user_verification_email.txt',
            {
                'user': self,
                'verification_url': request.build_absolute_uri(
                    reverse('user:user_verify', kwargs={
                        'uid': urlsafe_base64_encode(force_bytes(self.pk)),
                        'token': default_token_generator.make_token(self)
                    })
                )
            },
            [self.email]
        )
