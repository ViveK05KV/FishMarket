from django.shortcuts import render
from django.http import HttpResponse
import logging

from .models import *
# Create your views here.

def fish(request):
    available_fish_ids = fishcurrent.objects.values_list('fid', flat=True).exclude(currentfish = 0)
    available_fish = fishcurrent.objects.exclude(currentfish = 0)
    logger = logging.getLogger(__name__)
    tag = request.GET.get('name', None)

    all_fish = fishmain.objects.filter( pk__in = available_fish_ids )
    for i in all_fish:
        print(i.fishtype)
    marine_fish = all_fish.filter( fishtype = 'm' )
    fresh_fish = all_fish.filter( fishtype = 'f' )
    shell_fish = all_fish.filter( fishtype = 's' )
    return render(request, 'fish_market/marine.html' , {'available_fish' : available_fish ,'all_fish' : all_fish , 'marine_fish' : marine_fish , 'fresh_fish' : fresh_fish , 'shell_fish' : shell_fish })

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
