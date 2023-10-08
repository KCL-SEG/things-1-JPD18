from django.shortcuts import render
from .forms import ThingForm
# Create your views here.
def home(request):
    form = ThingForm()
    return render(request,'things/home.html',{'form':form})
