from django.conf.urls import patterns, url
from web.views import NuncBaseView
urlpatterns = patterns(
    '',
    url(r'^$', NuncBaseView.as_view(), name='index_view'),
)
