#-*- coding:utf-8 -*-
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_arguments):
        """
        creates user with email and password
        """
        now = timezone.now()
        user = self.model(
            username=username, 
            email=email, **extra_arguments
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        su = self.create_user(email, username, password, **extra_fields)
        su.is_staff = True
        su.is_active = True
        su.save(using=self._db)
        return su


class User(AbstractBaseUser):
    join_date = models.DateTimeField(_(u'생성일'), default=timezone.now, auto_now_add=True)
    gender = models.BooleanField(default=True, help_text=u'성별')
    birthday = models.DateField(null=True, blank=True)
    email = models.EmailField(_('Email'),
                              max_length=255,
                              db_index=True,
                              unique=True)

    phone_number = models.CharField(_(u'전화번호'),
                                    max_length=20,
                                    null=True)

    username = models.CharField(_(u'사용자 이름'),
                                 max_length=255,
                                 help_text=_(u'사용자 이름'))

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)    
    
    USERNAME_FIELD = 'email'
    objects = UserManager()    

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.username

        
    class Meta:
        verbose_name=_(u'사용자')
        verbose_name_plural = _(u'사용자들')
    

# class User(NuncUser):
