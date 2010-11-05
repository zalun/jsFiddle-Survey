from django.conf.urls.defaults import *
from django.views import static
from django.conf import settings

from spinner import views as spinner_views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    # main page
    url(r'^$', spinner_views.start_test),

    # media
    url(r'^files/(?P<path>.*)$', static.serve,
        {'document_root': settings.MEDIA_ROOT}, name='media'),

    # spinner
    (r'^spinner/', include('spinner.urls')),

    # echo
    (r'^echo/', include('echo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
