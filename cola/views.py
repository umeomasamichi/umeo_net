from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Cola

def index(request):
    return HttpResponse("wowwow")