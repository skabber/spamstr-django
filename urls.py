from django.conf.urls.defaults import *
from django.contrib import admin
from urlsLocal import urlpatterns as newPatterns
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^spamstr/', include('spamstr.foo.urls')),

    # Uncomment the next line to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'', include('spamstr.person.urls')),
#    (r'^$', 'spamstr.person.views.all')
)

urlpatterns += newPatterns