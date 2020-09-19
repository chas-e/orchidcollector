from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3
from decouple import config

from .models import Orchid, Supply, Photo
from .forms import WateringForm

S3_BASE_URL = config('S3_BASE_URL')
BUCKET = config('BUCKET')


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up, please try again.'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def orchids_index(request):
    orchids = Orchid.objects.filter(user=request.user)
    return render(request, 'orchids/index.html', { 'orchids': orchids })

@login_required
def orchids_detail(request, orchid_id):
    orchid = Orchid.objects.get(id=orchid_id)
    # Get supplies the orchid doesn't have
    supplies_orchid_doesnt_have = Supply.objects.exclude(id__in = orchid.supplies.all().values_list('id'))
    # instantiate WateringForm to be rendered in this template
    watering_form = WateringForm()
    return render(request, 'orchids/detail.html', { 'orchid': orchid, 'watering_form': watering_form, 'supplies': supplies_orchid_doesnt_have })

@login_required
def add_watering(request, orchid_id):
    form = WateringForm(request.POST)

    if form.is_valid():
        new_watering = form.save(commit=False)
        new_watering.orchid_id = orchid_id
        new_watering.save()

    return redirect('detail', orchid_id=orchid_id)

@login_required
def add_photo(request, orchid_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            photo = Photo(url=url, orchid_id=orchid_id)
            photo.save()
        except:
            print('An error ocurred uploading the file to s3.')
    return redirect('detail', orchid_id=orchid_id)

@login_required
def assoc_supply(request, orchid_id, supply_id):
    Orchid.objects.get(id=orchid_id).supplies.add(supply_id)
    return redirect('detail', orchid_id=orchid_id)

@login_required
def disassoc_supply(request, orchid_id, supply_id):
    Orchid.objects.get(id=orchid_id).supplies.remove(supply_id)
    return redirect('detail', orchid_id=orchid_id)

class OrchidCreate(LoginRequiredMixin, CreateView):
    model = Orchid
    fields = ['name', 'genus', 'description', 'age']

    # assign user to form when creating a new orchid
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class OrchidUpdate(LoginRequiredMixin, UpdateView):
    model = Orchid
    fields = '__all__'

class OrchidDelete(LoginRequiredMixin, DeleteView):
    model = Orchid
    success_url = '/orchids/'

class SupplyCreate(LoginRequiredMixin, CreateView):
    model = Supply
    fields = ['name', 'description']

class SupplyUpdate(LoginRequiredMixin, UpdateView):
    model = Supply
    fields = ['name', 'description']

class SupplyDelete(LoginRequiredMixin, DeleteView):
    model = Supply
    success_url = '/supplies/'

class SupplyDetail(LoginRequiredMixin, DetailView):
    model = Supply

class SupplyList(LoginRequiredMixin, ListView):
    model = Supply
