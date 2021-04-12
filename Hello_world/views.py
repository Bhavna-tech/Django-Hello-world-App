from django.shortcuts import render, HttpResponse

def show(request):
    return HttpResponse('<p>Hello World! <br> <br>\t I am Bhavna Latare a student of Government College of Engineering Jalgaon. <br> I am a pursuing Computer Engineering graduate studying in 3rd year. </p> ')
