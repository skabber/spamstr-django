from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^person/(?P<id>\d+)/$', 'spamstr.person.views.detail'),
    (r'^add/', 'spamstr.person.views.add'),
    (r'^delete/(?P<id>\d+)/$', 'spamstr.person.views.delete'),
    (r'^$', 'spamstr.person.views.all'),
)