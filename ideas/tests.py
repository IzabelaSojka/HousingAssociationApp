from django.test import TestCase

from .models import *
from .forms import BillingForm

class BillingTestCase(TestCase):
    def test_fields(self):
        admin = User.objects.create(username='chef', password='0987poi.,')
        resident = User.objects.create(username='resident', password='0987poi.,')
        local = Local.objects.create(admin=admin, owner=resident, number='1', area='50.50')
        model = Billing(
            admin = admin,
            owner = local,
            value= '1234.56',
            addressee_name= 'Bank',
            bank_account= '11122233344455566677788899',
            status= 'False',
            start_billing= '2022-12-12',
            end_billing= '2023-01-12',
            payment_date=  '2023-01-22',
        )
        model.save()

        self.assertEqual(model.value, '1234.56')
        self.assertEqual(model.addressee_name, 'Bank')
        self.assertEqual(model.bank_account, '11122233344455566677788899')
        self.assertEqual(model.status, 'False')
        self.assertEqual(model.start_billing, '2022-12-12')
        self.assertEqual(model.end_billing, '2023-01-12')
        self.assertEqual(model.payment_date, '2023-01-22')

class BillingFormTestCase(TestCase):
    def test_form_valid(self):
        admin = User.objects.create(username='chef', password='0987poi.,')
        resident = User.objects.create(username='resident', password='0987poi.,')
        local = Local.objects.create(admin=admin, owner=resident, number='1', area='50.50')
        form_data = {
            'admin': admin,
            'owner': local,
            'value': '1234,56',
            'addressee_name': 'Bank',
            'bank_account': '11122233344455566677788899',
            'status': 'False',
            'start_billing': '12.12.2022',
            'end_billing': '12.01.2023',
            'payment_date': '25.01.2023',
        }
        form = BillingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            'value': '1234,56',
            'addressee_name': 'Bank',
            'bank_account': '11122233344455566677788899',
            'status': 'False',
            'start_billing': '12.12.2022',
            'end_billing': '12.01.2023',
            'payment_date': '25.01.2023',
        }
        form = BillingForm(data=form_data)
        self.assertFalse(form.is_valid())

