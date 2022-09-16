from django.shortcuts import render
from django.http import HttpResponse
from .models import Cursus, PersonalTrainer, PasAanvraag

def begin_scherm(request):
    return render(request, 'begin_scherm.html')

# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')

def annuleer_abonnement(request):
    return render(request, 'annuleer_abonnement.html')

def personal_trainer(request):
    if request.method == "POST":
        date = request.POST.get('date')
        time = request.POST.get('time')
        personalTrainer = PersonalTrainer(User='TestUser', date=date, time=time)
        personalTrainer.save()
        return render(request, 'personal_trainer_succes.html', {'date': date, 'time': time})
    else:
        return render(request, 'personal_trainer.html')

def koop_cursus(request):
    return render(request, 'koop_cursus.html')

def koop_cursus2(request, cursus):
    if request.method == "POST":
        date = request.POST.get('date')
        cursus2 = Cursus(User='TestUser', date=date, cursus=cursus)
        cursus2.save()
        return render(request, 'cursus_succes.html', {'cursus': cursus, 'date': date})
    else:
        return render(request, 'koop_cursus2.html', {'cursus': cursus})

def pas_aanvragen(request):
    if request.method == "POST":
        voornaam = request.POST.get('voornaam')
        achternaam = request.POST.get('achternaam')
        email = request.POST.get('email')
        adres = request.POST.get('adres')
        pasaanvragen = PasAanvraag(voornaam=voornaam, achternaam=achternaam, email=email, adres=adres)
        pasaanvragen.save()
        return render(request, 'pas_aanvragen_succes.html', {'voornaam': voornaam, 'achternaam': achternaam})
    else:
        return render(request, 'pas_aanvragen.html')