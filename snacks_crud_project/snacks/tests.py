from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Snack
from django.urls import reverse


class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='bayan',
            email='bayankhatibtr@gmail.com',
            password='B12345678'
        )
        self.snack = Snack.objects.create(
            title='pizza',
            purshaser=self.user,
            description='tomato'
        )

    def test_snack_list_view(self):
        expected=200
        actual= self.client.get(reverse('snack_list')).status_code
        self.assertEqual(actual, expected)


    def test_snack_details_view(self):
        expected=200
        actual = self.client.get(reverse('snack_detail', args='1')).status_code
        self.assertEqual(expected, actual)


    def test_snack_create_view(self):
        expected=200
        actual = self.client.post(reverse('create_snack'),{'title': 'pizza', ' purshaser': self.user,'description': 'tomato',})
        self.assertEqual(expected, actual.status_code)
        self.assertContains(actual, 'tomato')
        self.assertContains(actual, 'bayan')
        


    def test_snack_update_view(self):
        expected=200
        actual = self.client.get(reverse('update_snack', args='1')).status_code
        self.assertEqual(expected, actual)


    def test_snack_delete_view(self):
        expected=200
        actual = self.client.get(reverse('delete_snack', args='1')).status_code
        self.assertEqual(expected, actual)

    
    def test_string_representation(self):
        snack_str = Snack(title='pizza')
        self.assertEqual(str(snack_str),self.snack.title)

    def test_all_fields(self):
        self.assertEqual(self.snack.title, 'pizza')
        self.assertEqual(str(self.snack.purshaser), 'bayan')
        self.assertEqual(self.snack.description, 'tomato')

  

  

   