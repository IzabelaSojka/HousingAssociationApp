from django.db import models
from django.conf import settings

class Administrator(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(("Name"), max_length=50)
    surname = models.CharField(("Surname"), max_length=50)

    def __str__(self):
        return 'Administrator profile {}.'.format(self.user.username)

class Local(models.Model):
    number = models.IntegerField()
    area = models.IntegerField()

    def __str__(self):
        return self.name