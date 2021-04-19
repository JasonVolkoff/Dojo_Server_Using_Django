from django.shortcuts import render, redirect, HttpResponseRedirect


def index(request):
    return render(request, "index.html")


def results(request):
    context = {
        "results": request.session["results"]
    }
    return render(request, "userIndex.html", context)


def createUser(request):
    if request.method == "POST":
        request.session["results"] = {
            "name": request.POST["userName"],
            "location": request.POST["userLocation"],
            "language": request.POST["userLanguage"],
            "comment": request.POST["userComment"]
        }
        return redirect("/results")
