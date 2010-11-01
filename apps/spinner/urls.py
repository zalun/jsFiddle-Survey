from django.conf.urls.defaults import *

urlpatterns = patterns(
    'spinner.views',
    # draft
    url(r'^$','start_test', name='spinner'),
    url(r'^thanks/$','thanks', name='spinner_thanks'),
    url(r'^fail/$','failure', name='spinner_failed'),
)
