from django.shortcuts import render
from .models import Assignment
from django.views import generic
# Create your views here.

class CustView(generic.DetailView):
    model=Assignment
    template_name='detail.html'

class HomeView(generic.ListView):
    queryset=Assignment.objects.filter(status=0)
    template_name='index_cust.html' 


class AboutView(generic.TemplateView):
    template_name='about_cust.html'
