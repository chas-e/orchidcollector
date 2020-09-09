from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Orchid

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def orchids_index(request):
    orchids = Orchid.objects.all()
    return render(request, 'orchids/index.html', { 'orchids': orchids })

def orchids_detail(request, orchid_id):
    orchid = Orchid.objects.get(id=orchid_id)
    return render(request, 'orchids/detail.html', { 'orchid': orchid })

class OrchidCreate(CreateView):
    model = Orchid
    fields = '__all__'