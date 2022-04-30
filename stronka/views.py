from django.shortcuts import render

from stronka.models import Description


def index(request):

    dests = Description.objects.all()

    return render(request, 'stronka/index.html', {'dests': dests})
