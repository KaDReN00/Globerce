from django.shortcuts import render

from .models import *
from .form import *


def intro(request):
    context = {}

    form = General_provisions(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "intro.html", context)


def smth(request):
    context = {}

    form = Smth(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "smth.html", context)


def detail_view(request, id):
    context = {"data": General_provisions.objects.get(id=id)}

    return render(request, "detail_view.html", context)
