from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Record, Song


def index(request):
    records = Record.objects.all()
    # template = loader.get_template('./music/index.html')
    context = {
        'records': records,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, './music/index.html', context)


def record_detail(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    return render(request, './music/details.html', {'record': record})
