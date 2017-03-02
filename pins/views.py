from django.http import HttpResponse
from django.shortcuts import render

from .models import Pins
# Create your views here.

def pins(request):
    # pins = Pins.objects.all()
