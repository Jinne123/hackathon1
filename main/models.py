from django.db import models


class Cursus(models.Model):
    User = models.CharField(max_length=30)
    date = models.DateField()
    cursus = models.CharField(max_length=30)


class PersonalTrainer(models.Model):
    User = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()


class PasAanvraag(models.Model):
    voornaam = models.CharField(max_length=30)
    achternaam = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    adres = models.CharField(max_length=30)