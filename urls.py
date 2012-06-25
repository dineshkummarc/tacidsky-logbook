from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^flight/(?P<flight>.*)/','logbook.views.flight'),
    (r'^$', 'logbook.views.index'),
)
