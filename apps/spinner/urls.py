from django.conf.urls.defaults import *

urlpatterns = patterns(
    'spinner.views',
    # draft
    url(r'^$','start_test', name='spinnser_start'),
    url(r'^result/$', 'get_results', name='spinner_result'),
)
