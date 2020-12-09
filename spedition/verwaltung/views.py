from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def index(request):
    template = 'spedition/index.html'
    return render(request,template,{})

def bestellung(request):
    if request.method =="GET":
        template = 'spedition/bestellung.html'
        kundends = Kunde.objects.all()
        return render(request,template,{'kunden':kundends})
    else:
        button = request.POST['button']
        if button == "cancel":
            return redirect("/")
        else:
            bestellungen = request.POST['bestellung'] 
            kunde = Kunde.objects.get(name=(request.POST['kunde']))
            print(kunde)
            ds = Bestellung(bestellung=bestellungen,kunde=kunde)
            ds.save()
            return redirect("/")