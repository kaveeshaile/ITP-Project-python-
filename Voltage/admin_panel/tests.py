from django.test import TestCase
from .models import events

# Create your tests here.

class eventTest(TestCase):
    def setUp(self):
        events.objects.create(Event_type='any',Location='Malabe',Contact='07646363633',Customer_ID='10',Date='2020-12-10',Status='waiting',OnCreateTime='2020-10-16 23:54:53')
        
    def testEvent(self):
            obj = events.objects.get(OnCreateTime ='2020-10-16 23:54:53')
            self.assertEqual(obj.OnCreateTime,'2020-10-16 23:54:53')