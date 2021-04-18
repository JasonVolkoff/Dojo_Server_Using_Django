from django.shortcuts import render, redirect, HttpResponseRedirect


def index(request):
    return render(request, "index.html")


def home(request):
    return HttpResponseRedirect("/")


def result(request):
    if request.method == "POST":
        context = {
            "name": request.POST["userName"],
            "language": request.POST["userLanguage"],
            "location": request.POST["userLocation"],
            "comment": request.POST["userComment"],
        }
        return render(request, "userIndex.html", context)
    return render(request, "userIndex.html")
