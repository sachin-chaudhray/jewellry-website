from django.urls import path
from .views import *

urlpatterns = [
    path('',home , name='home' ),
    path('jewellery/', jewellery, name='jewellery'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about')
]