from django.shortcuts import render, HttpResponse

def show(request):
    return HttpResponse('Hello World!')