import random

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from spinner.models import Result as SpinnerResult

def start_test(req, thanks=False, template='spinner/index.html'):
    """
    Display test with random values
    Get results from the POST if any
    Save the data
    """
    # check the survey response
    if req.method == 'POST':
        if req.POST.get('faster', False):
            # save data
            SpinnerResult.objects.create(
                xhr_duration=req.POST.get('xhr_duration'),
                spinner_delay_a=req.POST.get('spinner_delay_a'),
                spinner_delay_b=req.POST.get('spinner_delay_b'),
                faster=req.POST.get('faster')
            )
            return HttpResponseRedirect(reverse('spinner_thanks'))

    xhr_duration_set = ('0.2', '0.4', '0.6', '1.0', '1.5')
    spinner_delay_set = {
            '0.2': (0.0, 0.3),              # 0.3 will not show
            '0.4': (0.0, 0.2, 0.5),         # 0.5 will not show
            '0.6': (0.0, 0.2, 0.4, 0.7),    # 0.7 will not show
            '1.0': (0.0, 0.2, 0.4, 0.6),
            '1.5': (0.0, 0.2, 0.4, 0.6)
            }

    xhr_duration = random.choice(xhr_duration_set)
    spinner_delay_a = random.choice(spinner_delay_set[str(xhr_duration)])
    spinner_delay_b = random.choice(spinner_delay_set[str(xhr_duration)])
    xhr_duration = float(xhr_duration)

    return render_to_response(template, {
        'xhr_duration': xhr_duration,
        'spinner_delay_a': spinner_delay_a,
        'spinner_delay_b': spinner_delay_b,
        'thanks': thanks
        }, context_instance=RequestContext(req))


def thanks(req):
    """
    Show thanks with ability to take the survey again
    """
    return start_test(req, thanks=True)
