from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Farmer Produce Management System</h1>")
from django.shortcuts import render


