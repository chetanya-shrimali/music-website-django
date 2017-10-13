from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Record, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy


def index(request):
    records = Record.objects.all()
    # template = loader.get_template('./music/index.html')
    context = {
        'records': records,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, './music/index.html', context)


def record_detail(request, pk):
    record = get_object_or_404(Record, pk=pk)
    return render(request, './music/details.html', {'record': record})


class RecordCreate(CreateView):
    model = Record
    fields = ['artist_name', 'record_name', 'genre', 'record_logo']


class RecordUpdate(UpdateView):
    model = Record
    fields = ['artist_name', 'record_name', 'genre', 'record_logo']


class RecordDelete(DeleteView):
    model = Record
    success_url = reverse_lazy('music:index')
