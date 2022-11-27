from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Local(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin', null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)
    number = models.IntegerField(("Numer lokalu"), null=False, blank=False)
    area = models.DecimalField(("Powierzchnia"), max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = "local"
        verbose_name_plural = "local"

class Billing(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Local, on_delete=models.CASCADE, null=False, blank=False)
    value = models.DecimalField(("Kwota do zapłaty"), max_digits=100, decimal_places=2)
    status = models.BooleanField(("Czy zapłacone?"))
    start_billing = models.DateField(("Początek okresu rozliczeniowego"), null=False, blank=False)
    end_billing = models.DateField(("Koniec okresu rozliczeniowego"), null=False, blank=False)
    payment_date = models.DateField(("Termin płatności"), null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    id_b = models.OneToOneField(Billing, on_delete=models.CASCADE)
    number_local = models.ForeignKey(Local, on_delete=models.CASCADE, null=True, blank=False)

    def __str__(self):
        return str(self.id)


