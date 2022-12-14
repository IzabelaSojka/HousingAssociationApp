from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Local(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin', null=True, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owner', null=True, blank=True)
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
    addressee_name = models.TextField(("Adresat rachunku"), null=True, blank=True)
    bank_account = models.CharField(("Numer konta"), max_length=26, null=True, blank=True)
    status = models.BooleanField(("Czy zapłacone?"))
    start_billing = models.DateField(("Początek okresu rozliczeniowego"), null=False, blank=False)
    end_billing = models.DateField(("Koniec okresu rozliczeniowego"), null=False, blank=False)
    payment_date = models.DateField(("Termin płatności"), null=True, blank=True)
    details = models.FileField(("Szczegóły"), upload_to='', null=True)

    def __str__(self):
        return str(self.id)


class Report(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(("Nazwa pliku"), max_length=255, null=True)
    my_file = models.FileField(("Plik"), upload_to='', null=True)

    def __str__(self):
        return self.file_name

class Comemnt(models.Model):
    id_report = models.ForeignKey(Report, on_delete=models.CASCADE, null=False, blank=False)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    content = models.TextField(("Komentarz"), null=False, blank=False)

    def __str__(self):
        return str(self.id)