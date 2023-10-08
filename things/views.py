from django.shortcuts import render
from .forms import ThingForm
# Create your views here.
def home(request):
    form = ThingForm()
    return render(request,'things/add_thing.html',{'form':form})
