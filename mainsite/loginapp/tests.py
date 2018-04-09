from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
class LoginTest(TestCase):
    def setUp(self):
        self.credentials1 = {'username' : 'test1username',
                            'password' : 'test1password'}

        User.objects.create_user(**self.credentials1)

        self.credentials2 = {'username': 'test2username',
                            'password': 'test2password'}

        User.objects.create_user(**self.credentials2)
        self.credentials3 = {'username': 'test3username',
                            'password': 'test3password'}

        User.objects.create_user(**self.credentials3)

        self.credentials4 = {'username': 'test4username',
                            'password': 'test4password'}

        User.objects.create_user(**self.credentials4)

        self.credentials5 = {'username': 'test5username',
                            'password': 'test5password'}

        User.objects.create_user(**self.credentials5)

    def test_login(self):
        response = self.client.post('/login/', self.credentials1, follow = True)
        self.assertTrue(response.context['user'].is_active)

        response = self.client.post('/login/', self.credentials2, follow=True)
        self.assertTrue(response.context['user'].is_active)

        response = self.client.post('/login/', self.credentials3, follow=True)
        self.assertTrue(response.context['user'].is_active)

        response = self.client.post('/login/', self.credentials4, follow=True)
        self.assertTrue(response.context['user'].is_active)

        response = self.client.post('/login/', self.credentials5, follow=True)
        self.assertTrue(response.context['user'].is_active)