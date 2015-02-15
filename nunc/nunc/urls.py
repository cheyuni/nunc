from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.views import NuncBaseView, LoginView

urlpatterns = patterns('',
                       url(r'^$', NuncBaseView.as_view(), name='base_view'),
                       url(r'^login/$', LoginView.as_view(), name='login_view'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'card/', include('cards.urls')),
)
