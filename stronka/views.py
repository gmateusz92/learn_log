from django.shortcuts import render

from stronka.models import Description


def index(request):
    dest = Description()
    dest.name = 'elo'
    dest.desc = 'xxxx'
    dest.img = 'destination_1.jpg'
    dest.price = 800
    dest.offer = True

    dest1 = Description()
    dest1.name = 'ddd'
    dest1.desc = 'ddddddddddddd'
    dest1.img = 'destination_2.jpg'
    dest1.price = 900

    dests = [dest, dest1]

    return render(request, 'stronka/index.html', {'dests': dests})
