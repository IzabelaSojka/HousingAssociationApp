# Generated by Django 4.1.1 on 2022-12-14 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0012_remove_report_id_b_remove_report_number_local_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='addressee_name',
            field=models.TextField(blank=True, null=True, verbose_name='Adresat'),
        ),
        migrations.AddField(
            model_name='billing',
            name='bank_account',
            field=models.CharField(blank=True, max_length=26, null=True, verbose_name='Numer konta'),
        ),
        migrations.AddField(
            model_name='billing',
            name='details',
            field=models.FileField(null=True, upload_to='', verbose_name='Szczegóły'),
        ),
        migrations.AlterField(
            model_name='report',
            name='my_file',
            field=models.FileField(null=True, upload_to='', verbose_name='Plik'),
        ),
        migrations.CreateModel(
            name='Comemnt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Komentarz')),
                ('id_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.report')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]