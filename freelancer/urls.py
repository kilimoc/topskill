from django.urls import path
from . import  views
app_name='freelancer'

urlpatterns=[
    path('signup/',views.registerFreelancer,name='f_signup'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate_account, name='activate'),
]