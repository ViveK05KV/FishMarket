from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
import logging
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from .models import *
from .forms import *
import json
from django.core import serializers
from django.http import JsonResponse
# Create your views here.

def cart_after_login(request):
    if request.user.is_authenticated() and request.user.is_superuser:
        orderdetails = order.objects.all()
        items = CartItem.objects.all()
        return render(request,'fish_market/admin.html' , {'order' : orderdetails,'items' : items})
    else:
        return HttpResponseRedirect("/fish/home")

def registerpage(request):
    return render(request,'fish_market/register.html')

def fish(request):
    available_fish_ids = fishcurrent.objects.values_list('fid', flat=True).exclude(currentfish__lt=3)
    available_fish = fishcurrent.objects.exclude(currentfish__lt=3)
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
    tag = request.GET.get('name', None)


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


def getitems(request):
    postdata = request.POST.copy()
    idd = postdata.get('id','')
    print("________________________________")
    print(idd)
    citems = CartItem.objects.filter(cart_id = 'B@sXT*qSs9acVg&UwQfpLfBRip$%fQkAk41vaB%IH#^NHnUsdK')
    for i in citems:
        print(i)
    arr = []
    for data in citems:
        arr.append({
            'cart_id': data.cart_id,
            'date_added': data.date_added,
            'quantity': data.quantity,
            'product': data.product,
            'ft': data.ft,
        },)
    print("Ok")
    #data = serializers.serialize('json', arr)
    #data = serializers.serialize('json', [citems,])
    #return JsonResponse(arr, safe=True)
    data = serializers.serialize("json", citems)
    #return HttpResponse(data, mimetype='application/json')
    #return HttpResponse(data, content_type='application/json')
    #return HttpResponse(json.dumps(arr), content_type="application/json")
    #return HttpResponse(citems)
    return HttpResponse(json.dumps(data))
