from django.shortcuts import render
from django.http import HttpResponse


def word_counter(request):
    return HttpResponse("hi")
