from django.urls import path
from app1.views import *
app_name='login_page'

urlpatterns=[
    path('login/',login,name='login')
]