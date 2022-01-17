from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def problem(request):
    return render(request, 'problem.html')
