from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint

# Create your views here.

def simple_view(requests):
    pprint(requests.__dict__)
    return HttpResponse("Hello")