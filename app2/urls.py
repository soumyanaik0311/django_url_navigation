from django.urls import path
from app2.views import *
app_name='registration_page'

urlpatterns=[
    path('registration/',registration,name='registration')
]