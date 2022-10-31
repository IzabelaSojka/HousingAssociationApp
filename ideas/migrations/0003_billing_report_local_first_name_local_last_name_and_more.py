# Generated by Django 4.1.1 on 2022-10-31 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0002_local'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Kwota do zapłaty')),
                ('status', models.BooleanField(verbose_name='Czy zapłacone?')),
                ('start_billing', models.DateField(verbose_name='Początek okresu rozliczeniowego')),
                ('end_billing', models.DateField(verbose_name='Koniec okresu rozliczeniowego')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='pdf/', verbose_name='Plik')),
                ('id_b', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ideas.billing')),
            ],
        ),
        migrations.AddField(
            model_name='local',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Imię'),
        ),
        migrations.AddField(
            model_name='local',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nazwisko'),
        ),
        migrations.AddField(
            model_name='local',
            name='name_account',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Właściciel'),
        ),
        migrations.AddField(
            model_name='local',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='local',
            name='area',
            field=models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Powierzchnia'),
        ),
        migrations.AlterField(
            model_name='local',
            name='number',
            field=models.IntegerField(verbose_name='Numer lokalu'),
        ),
        migrations.DeleteModel(
            name='Administrator',
        ),
        migrations.AddField(
            model_name='report',
            name='number_local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.local'),
        ),
        migrations.AddField(
            model_name='billing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.local'),
        ),
    ]
