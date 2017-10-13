from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, redirect
from .models import Record, Song
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


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


class UserFormView(View):
    form_class = UserForm
    template_name = './registration_form'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()