from django.conf.urls.defaults import *

urlpatterns = patterns(
    'spinner.views',
    # draft
    url(r'^$','start_test', name='spinner'),
)
