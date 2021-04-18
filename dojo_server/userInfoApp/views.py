from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def result(request):
    return render(request, "userIndex.hmtl", context)
