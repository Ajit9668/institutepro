from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.registerview,name='register'),
    path('',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('home/',views.homeview,name='home'),
    path('contact/',views.contactview,name='contact'),
    path('service/',views.serviceview,name='service'),
    path('gallery/',views.galleryview,name='gallery'),
    path('feedback/',views.feedbackview,name='feedback'),

]