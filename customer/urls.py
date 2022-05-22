from . import views
from django.urls import path
from django.contrib import admin

urlpatterns =[
    path('', views.HomeView.as_view(), name='home_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('<slug:slug>', views.CustView.as_view(), name='detail_view')

]