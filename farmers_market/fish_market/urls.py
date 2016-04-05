from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    url(r'^home', views.fish),
    url(r'^login/home', views.fish),
    url(r'^marine', views.marine),
    url(r'^fresh', views.fresh),
    url(r'^shell', views.shell),
    url(r'^fishDetails/$', views.fishDetails , name='details' ),
    url(r'^one/(?P<id>\d+)$',views.fishone, name='fishone' ),
    url(r'^login/action/', views.loginaction ),
    url(r'^login/', views.loginview ),
    url(r'^logout/', views.logoutaction ),
    url(r'^register/', views.registeraction ),

]

urlpatterns += staticfiles_urlpatterns()
