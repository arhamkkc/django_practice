from django.contrib import admin
from django.urls import path,include
from basic_app_four import views

app_name='basic_app_four'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
    path('base/',views.base,name='base')
]
