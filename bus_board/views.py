from django.shortcuts import render, redirect


def home(request):
    '''
    view function for landing page
    '''
    return render(request, 'home.html')
