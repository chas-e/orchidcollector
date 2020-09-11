from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Orchid, Supply
from .forms import WateringForm


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
    # Get supplies the orchid doesn't have
    supplies_orchid_doesnt_have = Supply.objects.exclude(id__in = orchid.supplies.all().values_list('id'))
    # instantiate WateringForm to be rendered in this template
    watering_form = WateringForm()
    return render(request, 'orchids/detail.html', { 'orchid': orchid, 'watering_form': watering_form, 'supplies': supplies_orchid_doesnt_have })

def add_watering(request, orchid_id):
    form = WateringForm(request.POST)

    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.orchid_id = orchid_id
        new_watering.save()

    return redirect('detail', orchid_id=orchid_id)

def assoc_supply(request, orchid_id, supply_id):
    Orchid.objects.get(id=orchid_id).supplies.add(supply_id)
    return redirect('detail', orchid_id=orchid_id)

def disassoc_supply(request, orchid_id, supply_id):
    Orchid.objects.get(id=orchid_id).supplies.remove(supply_id)
    return redirect('detail', orchid_id=orchid_id)

class OrchidCreate(CreateView):
    model = Orchid
    fields = ['name', 'genus', 'description', 'age']

class OrchidUpdate(UpdateView):
    model = Orchid
    fields = '__all__'

class OrchidDelete(DeleteView):
    model = Orchid
    success_url = '/orchids/'

class SupplyCreate(CreateView):
    model = Supply
    fields = ['name', 'description']

class SupplyUpdate(UpdateView):
    model = Supply
    fields = ['name', 'description']

class SupplyDelete(DeleteView):
    model = Supply
    success_url = '/supplies/'

class SupplyDetail(DetailView):
    model = Supply

class SupplyList(ListView):
    model = Supply
