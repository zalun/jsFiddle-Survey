from django.conf.urls.defaults import *

urlpatterns = patterns('echo.views',
    url(r'^html/$', 'echo_html', name='echo_html')
)
