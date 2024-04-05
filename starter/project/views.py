from django.http import HttpRequest
from django.shortcuts import render


def display(request):
    return render(request, "I'm learning Django with Microsoft learn...")