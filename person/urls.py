from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^person/(?P<id>\d+)/$', 'spamstr.person.views.detail'),
    (r'^add/$', 'spamstr.person.views.add_or_edit', {'id': None}),
    (r'^edit/(?P<id>\d+)/$', 'spamstr.person.views.add_or_edit'),
    (r'^delete/(?P<id>\d+)/$', 'spamstr.person.views.delete'),
    (r'^$', 'spamstr.person.views.index'),
)