from django.conf.urls import patterns, url

from users.views import profile

urlpatterns = patterns(
    '',
    url(r'^profile/$', profile, name='profile'),
)
