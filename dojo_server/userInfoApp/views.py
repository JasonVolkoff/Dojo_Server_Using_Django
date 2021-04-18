from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def result(request):
    print(request.method)
    return render(request, "userIndex.html")
