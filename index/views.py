from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'index.html')


def problem(request):
    return render(request, 'problem.html')


def health(request):
    return HttpResponse(request, status=200)
