#-*- coding:utf-8 -*-
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from users.models import User

# Create your models here.

class Card(models.Model):
    pub_date = models.DateTimeField(_(u'생성일'), default=timezone.now, auto_now_add=True)
    users = models.ManyToManyField(User, help_text=_(u'사용자'))    
    name = models.CharField(_(u'카드 이름'), max_length=30)
    like_count = models.IntegerField(help_text=_(u'좋아요 갯수'))

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-id']
        verbose_name = _(u'카드')
        verbose_name_plural = _(u'카드')
    
class Video(models.Model):
    pub_date = models.DateTimeField(_(u'생성일'), default=timezone.now, auto_now_add=True)
    card = models.ForeignKey(Card, help_text=_(u'속한카드'))
    title = models.CharField(max_length=100, help_text=_(u'실제 영상 제목'))
    query = models.CharField(max_length=100, help_text=_(u'사용자 쿼리'))
    key = models.CharField(max_length=30, help_text=_(u'유투브 키'))

    
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = _(u'영상')
        verbose_name_plural = _(u'영상')
