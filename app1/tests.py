from django.test import TestCase
from app1.models import Customer, Product

# Create your tests here.


class CustomerTest(TestCase):
    def test_model(self):
        c1 = Customer.objects.create(name="Arjun kapoor", address='Panhala')
        self.assertEqual(c1.name, 'Arjun kapoor')
        self.assertTrue(c1.address, 'Panhala')

