from django.urls import path

from pybo import views

app_name = 'pyboapp'
urlpatterns =[
    path('',views.index),
]