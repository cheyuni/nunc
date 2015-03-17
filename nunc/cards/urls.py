from django.conf.urls import patterns, url
from cards.views import CardView, VideoView, profile

urlpatterns = patterns('',
                       url(r'^$', CardView.as_view(), name="card"),
                       url(r'(?P<card_id>\d+)', VideoView.as_view(), name="card"),
                       url(r'^profile/$', profile, name='profile'),                       
                       )
