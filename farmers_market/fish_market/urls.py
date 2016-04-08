from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from . import cart

urlpatterns = [
    url(r'^home', views.fish),
    url(r'^marine', views.marine),
    url(r'^fresh', views.fresh),
    url(r'^shell', views.shell),
    url(r'^fishDetails/$', views.fishDetails , name='details' ),
    url(r'^one/(?P<id>\d+)$',views.fishone, name='fishone' ),
    url(r'^one/showcart/deleteitem/',cart.remove_from_cart),
    url(r'^one/create_cookie/',cart.create_cookie),
    url(r'^one/showcart/',cart.showcart),

]

urlpatterns += staticfiles_urlpatterns()
