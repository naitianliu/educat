from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

# Create your views here.


@login_required
def home_panel(request):
    data = dict(
        page="summary"
    )
    return render_to_response('home/panel.html', data, RequestContext(request))