from django.shortcuts import render, redirect

def things (request):
    return render (request, 'things.html')