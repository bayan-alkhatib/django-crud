from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Snack
from django.urls import reverse


class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='bayan',
            email='bayankhatibtr@gmail.com',
            password='Bya@0143575'
        )
        self.post = Snack.objects.create(
            title='pizza',
            purshaser=self.user,
            description='tomato'
        )

    def test_string_representation(self):
        post = Snack(title='title')
        self.assertEqual(str(post), post.title)

    def test_all_fields(self):
        self.assertEqual(str(self.post), 'pizza')
        self.assertEqual(f'{self.post.purshaser}', 'bayan')
        self.assertEqual(self.post.description, 'tomato')


    def test_snack_list_view(self):
        response = self.client.get(reverse('snack_list'))
        self.assertEqual(response.status_code, 200)

    def test_snack_details_view(self):
        response = self.client.get(reverse('snack_detail', args='1'))
        self.assertEqual(response.status_code, 200)


    def test_snack_update_view(self):
        response = self.client.post(reverse('update_snack', args='1'), {
            'title': 'pizza',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'pizza')


    def test_snack_list_status(self):
        expected = 200
        url = reverse('snack_list')
        response = self.client.get(url)
        actual = response.status_code
        self.assertEquals(expected, actual)


    def test_create_view(self):
        response = self.client.post(reverse('create_snack'), {
            'title': 'pizza',
            ' purshaser': self.user,
            'description': 'tomato',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'pizza')
        self.assertContains(response, 'tomato')
        self.assertContains(response, 'bayan')


    def test_delete_view(self):
        response = self.client.get(reverse('delete_snack', args='1'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,'delete Snacks')
        post_response = self.client.post(reverse('delete_snack', args='1'))
        self.assertRedirects(post_response, reverse(
            'snack_list'), status_code=302)