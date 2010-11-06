from django.conf.urls.defaults import *

urlpatterns = patterns(
    'spinner.views',
    # draft
    url(r'^$','index', name='spinner_home'),
    url(r'^test/$','start_test', name='spinner_start'),
    url(r'^thanks/$','thanks', name='spinner_thanks'),
    url(r'^fail/$','failure', name='spinner_failed'),
    url(r'^data/$','get_data', name='spinner_data'),
    url(r'^results/$','results', name='spinner_results'),
)
