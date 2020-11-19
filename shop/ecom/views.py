from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

tasks = []


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New task")

# Create your views here


def index(request):
    return render(request, "index.html", {
        "tasks": tasks
    })


def test(request):
    now = datetime.datetime.now()
    return render(request, "index.html", {
        "newyear": now.month == 1 and now.day == 1
    })


def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "add.html", {
                "form": form
            })
    else:
        return render(request, "add.html", {
            "form": NewTaskForm
        })


def health_check(request):
    return HttpResponse("OK")


def dashboard(request):
    return HttpResponse("OK")


def product(request):
    return HttpResponse("OK")


def add_shop(request):
    pass


def add_product(request):
    pass


