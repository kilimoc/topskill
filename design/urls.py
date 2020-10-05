from django.urls import path

from design import views

app_name='design'

urlpatterns=[
    path('',views.HomeView.as_view(),name='home'),
    path('signin/',views.SignIn.as_view(),name='signin'),
    path('user/verificationsent/',views.SignUpSuccess.as_view(),name='verificationsent'),
]