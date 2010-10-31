from django.conf.urls.defaults import *

urlpatterns = patterns('echo.views',
    url(r'^echo/html/$', 'echo_html', name='echo_html')
)
