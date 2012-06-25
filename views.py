from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from django.conf import settings
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

from logbook.models import LogBookEntry


@login_required
def index(request):
    logs = LogBookEntry.objects.order_by('flight_date').filter(username=request.user)
    total_time = 0
    total_landings= 0
    for l in logs:
        total_time += l.total_duration_of_flight 
        total_landings += l.number_landings

    return render_to_response('logbook/index.html',
        {
        'logs':logs,
        'total_time':total_time,
        'total_landings':total_landings,
        })

 
@login_required
def flight(request,flight):
    log = get_object_or_404(LogBookEntry,pk=flight)
    return render_to_response('logbook/flight.html',
        {
        'log':log,
        })
