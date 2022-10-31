from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Local(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    number = models.IntegerField(("Numer lokalu"), null=False, blank=False)
    area = models.DecimalField(("Powierzchnia"), max_digits=100, decimal_places=2)
    name_account = models.CharField(("Właściciel"),max_length=255, null=True, blank=True)
    first_name = models.CharField(("Imię"), max_length=255, null=True, blank=True)
    last_name = models.CharField(("Nazwisko"), max_length=255, null=True, blank=True)

    def __str__(self):
        return self.number


class Billing(models.Model):
    owner = models.ForeignKey(Local,on_delete=models.CASCADE, null=False, blank=False)
    value = models.DecimalField(("Kwota do zapłaty"), max_digits=100, decimal_places=2)
    status = models.BooleanField(("Czy zapłacone?"))
    start_billing = models.DateField(("Początek okresu rozliczeniowego"), null=False, blank=False)
    end_billing = models.DateField(("Koniec okresu rozliczeniowego"), null=False, blank=False)

    def __str__(self):
        return self.id


class Report(models.Model):
    id_b = models.OneToOneField(Billing, on_delete=models.CASCADE)
    file = models.FileField(("Plik"), upload_to='pdf/')
    number_local = models.ForeignKey(Local, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.id