import time
from django.http import Http404, HttpResponse
from django.conf import settings

def echo_html(req):
    " respond with POST['html'] "
    if req.POST.get('delay', False):
        time.sleep(min(settings.MAX_DELAY, float(req.POST.get('delay'))))
    return HttpResponse(req.POST.get('html', ''))

