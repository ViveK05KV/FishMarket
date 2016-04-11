from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import logging
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from .models import *
from .forms import *
# Create your views here.

def cart_after_login(request):
    return HttpResponseRedirect("/fish/home")

def registerpage(request):
    return render(request,'fish_market/register.html')
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


@csrf_exempt
def register(request, template_name="registration/register.html"):
    """ view displaying customer registration form """
    if request.method == 'POST':
        print("request method is post" )
        postdata = request.POST.copy()
        form = RegistrationForm(postdata)
        if form.is_valid():
            #form.save()
            user = form.save(commit=False)  # new
            user.email = postdata.get('email','')  # new
            user.save()  # new
            un = postdata.get('username','')
            pw = postdata.get('password1','')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = urlresolvers.reverse('my_account')
                return HttpResponseRedirect(url)
    else:
        print("RegistrationForm is valid" )
        form = RegistrationForm()
    page_title = 'User Registration'
    return render(request, 'fish_market/success.html' )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/fish/home")
