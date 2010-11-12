import random

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Q

from spinner.models import Result as SpinnerResult


def index(req, template_prefix='spinner/'):
    """
    Display the Survey info
    """

    return render_to_response('%sindex.html' % template_prefix, {},
            context_instance=RequestContext(req))

def get_data(req, template_prefix='spinner/'):
    """
    Return all data as csv
    """
    response = render_to_response('%sresults.csv' % template_prefix, {
        'results': SpinnerResult.objects.all()})

    response['Content-Disposition'] = ("attachment; "
        "filename=spinner_survey_results.csv")

    return response
    #    mimetype='application/Excel')

def results(req, template_prefix='spinner/'):
    """
    Collect results and present in tabular form
    """
    #                    A      A    A     A
    #table = [       ['0.0','0.2','0.4','0.6'],
    # B        ['0.0',   2,   66,   12,   25],
    # B        ['0.2',   1,   12,    1,    1]
    # B       ...
    #        ]
    faster_no_order = {}
    faster_order = {}
    label = ('0.0', '0.2', '0.4', '0.6', 'x')  # 'x' represents 0.3, 0.5, 0.7
    for a in label:
        faster_order[a] = {}
        for b in label:
            if a != 'x' and b != 'x':
                query = Q(
                    spinner_delay_a=b,
                    spinner_delay_b=a
                )
            else:
                if a == 'x':
                    a_subquery = Q(spinner_delay_b=0.3) | \
                            Q(spinner_delay_b=0.5) | \
                            Q(spinner_delay_b=0.7)
                else:
                    a_subquery = Q(spinner_delay_b=a)
                if b == 'x':
                    b_subquery = Q(spinner_delay_a=0.3) | \
                            Q(spinner_delay_a=0.5) | \
                            Q(spinner_delay_a=0.7)
                else:
                    b_subquery = Q(spinner_delay_a=b)

                query = Q(a_subquery, b_subquery)

            _all = SpinnerResult.objects.filter(query)
            faster = _all.filter(faster='a').count() * 1.0
            slower = _all.filter(faster='b').count() * 1.0
            errors = _all.filter(broken=1).count() * 1.0
            total = _all.count()
            if total > 0:
                faster_order[a][b] = (int((faster - slower) / total * 100),
                                          int(errors / total * 100))

    for a in label:
        faster_no_order[a] = {}
        for b in label:
            if a != b:
                if a == 'x':
                    al_subquery = Q(spinner_delay_b=0.3) | \
                        Q(spinner_delay_b=0.5) | \
                        Q(spinner_delay_b=0.7)
                    ar_subquery = Q(spinner_delay_a=0.3) | \
                            Q(spinner_delay_a=0.5) | \
                            Q(spinner_delay_a=0.7)
                else:
                    al_subquery = Q(spinner_delay_b=a)
                    ar_subquery = Q(spinner_delay_a=a)

                if b == 'x':
                    bl_subquery = Q(spinner_delay_a=0.3) | \
                            Q(spinner_delay_a=0.5) | \
                            Q(spinner_delay_a=0.7)
                    br_subquery = Q(spinner_delay_b=0.3) | \
                        Q(spinner_delay_b=0.5) | \
                        Q(spinner_delay_b=0.7)
                else:
                    bl_subquery = Q(spinner_delay_a=b)
                    br_subquery = Q(spinner_delay_b=b)

                _left = SpinnerResult.objects.filter(
                    Q(al_subquery, bl_subquery))
                _right = SpinnerResult.objects.filter(
                    Q(ar_subquery, br_subquery))


                faster = _left.filter(faster='a').count() + \
                         _right.filter(faster='b').count() * 1.0
                slower = _left.filter(faster='b').count() + \
                         _right.filter(faster='a').count() * 1.0
                errors = _left.filter(broken=1).count() + \
                         _right.filter(broken=1).count() * 1.0
                total = _left.count() + _right.count() * 1.0
                if total > 0:
                    faster_no_order[a][b] = (int((faster - slower) / total*100),
                                          int(errors / total * 100))

    return render_to_response('%sresults.html' % template_prefix, {
        'faster_order': faster_order,
        'faster_no_order': faster_no_order,
        'overall': SpinnerResult.objects.count(),
        'labels': label
    }, context_instance=RequestContext(req))


def start_test(req, stage='start', template_prefix='spinner/'):
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
                faster=req.POST.get('faster'),
                broken=req.POST.get('broken', False)
            )
            return HttpResponseRedirect(reverse('spinner_thanks'))
        else:
            return HttpResponseRedirect(reverse('spinner_failed'))


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

    return render_to_response('%stest.html' % template_prefix, {
        'xhr_duration': xhr_duration,
        'spinner_delay_a': spinner_delay_a,
        'spinner_delay_b': spinner_delay_b,
        'stage_template': '%s_%s.html' % (template_prefix, stage)
        }, context_instance=RequestContext(req))


def thanks(req):
    """
    Show thanks with ability to take the survey again
    """
    return start_test(req, stage='thanks')

def failure(req):
    """
    Show thanks with ability to take the survey again
    """
    return start_test(req, stage='error')
