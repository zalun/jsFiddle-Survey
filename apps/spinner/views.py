import random

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from spinner.models import Result as SpinnerResult

def start_test(req, thanks=False, template='spinner/index.html'):
    """
    Display test with random values
    """
    xhr_length_set = ('1.0', '3.0', '5.0')
    spinner_delay_set = {
            '1.0': (0.0, 0.2, 0.4),
            '3.0': (0.0, 0.4, 1.0),
            '5.0': (0.0, 0.4, 1.0)
            }

    xhr_length = random.choice(xhr_length_set)
    spinner_delay_a = random.choice(spinner_delay_set[str(xhr_length)])
    spinner_delay_b = random.choice(spinner_delay_set[str(xhr_length)])
    xhr_length = float(xhr_length)

    return render_to_response(template, {
        'xhr_length': xhr_length,
        'spinner_delay_a': spinner_delay_a,
        'spinner_delay_b': spinner_delay_b,
        'thanks': thanks
        }, context_instance=RequestContext(req))


def get_results(req, template='spinner/index.html'):
    """
    Get results from the POST
    Save the data
    Call start_test
    """
    return start_test(req, thanks=True, template=template)


