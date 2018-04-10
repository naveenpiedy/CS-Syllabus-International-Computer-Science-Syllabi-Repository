from django.contrib.auth.models import User
from django.test import TestCase


# Create your tests here.
class LoginTest(TestCase):
    def setUp(self):
        self.userinfo1 = {'username': 'test1username',
                          'password': 'test1password',
                          'first_name': 'test1first_name',
                          'last_name': 'test1last_name',
                          'email': 'test1email@test.edu',
                          'university': 'ASU',
                          'isprofessor': 'True'}

        self.credentials1 = {'username': 'test1username',
                             'password': 'test1password'}

        User.objects.create_user(**self.userinfo1)

        self.userinfo2 = {'username': 'test2username',
                          'password': 'test2password',
                          'first_name': 'test2first_name',
                          'last_name': 'test2last_name',
                          'email': 'test2email@test.edu',
                          'university': 'ASU',
                          'isprofessor': 'True'}

        self.credentials2 = {'username': 'test2username',
                             'password': 'test2password'}

        User.objects.create_user(**self.userinfo2)
        self.userinfo3 = {'username': 'test3username',
                          'password': 'test3password',
                          'first_name': 'test3first_name',
                          'last_name': 'test3last_name',
                          'email': 'test3email@test.edu',
                          'university': 'ASU',
                          'isprofessor': 'True'}

        self.credentials3 = {'username': 'test3username',
                             'password': 'test3password'}

        User.objects.create_user(**self.userinfo3)

        self.userinfo4 = {'username': 'test4username',
                          'password': 'test4password',
                          'first_name': 'test4first_name',
                          'last_name': 'test4last_name',
                          'email': 'test4email@test.edu',
                          'university': 'ASU',
                          'isprofessor': 'True'}

        self.credentials4 = {'username': 'test4username',
                             'password': 'test4password'}

        User.objects.create_user(**self.userinfo4)

        self.userinfo5 = {'username': 'test5username',
                          'password': 'test5password',
                          'first_name': 'test5first_name',
                          'last_name': 'test5last_name',
                          'email': 'test5email@test.edu',
                          'university': 'ASU',
                          'isprofessor': 'True'}

        self.credentials5 = {'username': 'test5username',
                             'password': 'test5password'}

        User.objects.create_user(**self.userinfo5)

    def test_login(self):
        self.client.login(**self.credentials1)
        response = self.client.post('/login/', self.userinfo1, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.client.logout()

        self.client.login(**self.credentials2)
        response = self.client.post('/login/', self.userinfo2, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.client.logout()

        self.client.login(**self.credentials3)
        response = self.client.post('/login/', self.userinfo3, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.client.logout()

        self.client.login(**self.credentials4)
        response = self.client.post('/login/', self.userinfo4, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.client.logout()

        self.client.login(**self.credentials5)
        response = self.client.post('/login/', self.userinfo5, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.client.logout()
