from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from . import cart
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from fish_market.forms import RegistrationForm

urlpatterns = [
    url(r'^home', views.fish),
        url('^register/', CreateView.as_view(
                template_name='registration/register.html',
                form_class=RegistrationForm,
                success_url='/fish/home'
        ),
        name='registration'),
         url(
            r'^login/$',
            'django.contrib.auth.views.login',
            name='login',
            kwargs={'template_name': 'registration/login.html'}
        ),
    url(r'^logout/$',views.logout_view),
    url('^accounts/', include('django.contrib.auth.urls')),
    url('^accounts/login/getvalue/',  views.getitems),
    url('^accounts/login/home',  views.cart_after_login),
    url(r'^userregister', views.register),
    url(r'^home', views.fish),
    url(r'^marine', views.marine),
    url(r'^fresh', views.fresh),
    url(r'^shell', views.shell),
    url(r'^fishDetails/$', views.fishDetails , name='details' ),
    url(r'^one/(?P<id>\d+)$',views.fishone, name='fishone' ),
    url(r'^one/showcart/deleteitem/',cart.remove_from_cart),
    url(r'^one/showcart/emptycart/',cart.empty_cart),
    url(r'^one/create_cookie/',cart.create_cookie),
    url(r'^one/showcart/thanks',cart.thanks),
    url(r'^one/showcart/checkout/sub',cart.subform),
    url(r'^one/showcart/checkout',cart.checkout),
    url(r'^one/showcart/',cart.showcart),


]

urlpatterns += staticfiles_urlpatterns()
