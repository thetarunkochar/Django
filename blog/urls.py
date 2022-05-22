from . import views
from django.urls import path
from django.contrib import admin

urlpatterns =[
    # path('about', views.AboutView.as_view(), name='about_view'),
    
    path('',views.HomeView.as_view(), name='home_view'),
    path('about/', views.AboutView.as_view(), name='about_view'),
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    path('transfer/', views.transfer_data, name='transfer_view')
]

admin.site.site_header = "Mysite Admin"
admin.site.site_title = "Mysite Admin Portal"
admin.site.index_title = "hello"