from django.shortcuts import render
from django.http import HttpResponse
import logging
from django import forms
from django.middleware.csrf import CsrfViewMiddleware
from django.template import RequestContext
from .models import *
from django.shortcuts import render_to_response
from django.contrib.sessions.middleware import SessionMiddleware
import datetime
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Max
from django.http import HttpRequest
from datetime import datetime, timedelta
import decimal
import random
import json
# Create your views here.

def fish(request):
    available_fish_ids = fishcurrent.objects.values_list('fid', flat=True).exclude(currentfish = 0)
    available_fish = fishcurrent.objects.exclude(currentfish = 0)
    logger = logging.getLogger(__name__)
    tag = request.GET.get('name', None)

    all_fish = fishmain.objects.filter( pk__in = available_fish_ids )
    marine_fish = all_fish.filter( fishtype = 'm' )
    fresh_fish = all_fish.filter( fishtype = 'f' )
    shell_fish = all_fish.filter( fishtype = 's' )
    return render(request, 'fish_market/marine.html' , {'available_fish' : available_fish ,'all_fish' : all_fish , 'marine_fish' : marine_fish , 'fresh_fish' : fresh_fish , 'shell_fish' : shell_fish })

def fishone(request, id):
    fish=fishmain.objects.get(fid=id);
    rate=fishcurrent.objects.get(fid=id);
    return render(request,'fish_market/afish.html' , { 'fish' :fish , 'rate' :rate })

def marine(request):
    fish_market = FishDB.objects.filter( category = 'marine' )
    return render(request, 'fish_market/marine.html' , {'fish_market' : fish_market})

def fresh(request):

    fish_market = FishDB.objects.filter( category = 'Fresh Water' )
    return render(request, 'fish_market/marine.html' , {'fish_market' : fish_market})

def shell(request):
    fish_market = FishDB.objects.filter( category = 'Shell Fish' )
    return render(request, 'fish_market/marine.html' , {'fish_market' : fish_market})

def fishDetails(request):
# Get an instance of a logger
    logger = logging.getLogger(__name__)
    tag = request.GET.get('name', None)
    logger.error("the tag is "+ tag)

    try:
        fishThings = FishDB.objects.filter( name = tag )
    except fishThings.DoesNotExist:
        raise Http404
    return render(request, 'fish_market/afish.html' , {'fish_market' : fishThings})



def loginview(request):
    return render(request, 'fish_market/login.html' )


def loginaction(request):
    postdata = request.POST.copy()

    try:
        user = login.objects.get(username=postdata.get('username',''))
        if user.password == postdata.get('password',''):
            request.session['user_id'] = user.id
            data = {'userid':user.id}
            print(request.session['user_id'])
        else:
            request.session['user_id'] = 0
            del request.session['user_id']
            data = {'userid':0}
    except Exception as e:
        print("Error")
        request.session['user_id'] = 0
        del request.session['user_id']
        data = {'userid':0}

    return HttpResponse(json.dumps(data))

def logoutaction(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")


def registeraction(request):
    return render(request, 'fish_market/register.html' )
