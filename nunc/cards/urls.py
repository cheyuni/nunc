from django.conf.urls import patterns, url
from cards.views import CardView

urlpatterns = patterns('',
                       url(r'^$', CardView.as_view(), name="card"),
                       )
