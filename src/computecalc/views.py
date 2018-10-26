from django.shortcuts import render
from django.views.generic.list import ListView
from computecalc.models import Computecalc

# Create your views here.
class ComputecalcList(ListView):
    queryset = Computecalc.objects.all()
    template_name = "calclist.html"
    model = Computecalc
