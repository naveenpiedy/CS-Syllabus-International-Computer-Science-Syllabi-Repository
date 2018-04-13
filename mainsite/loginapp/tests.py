from loginapp.models import UserTable
from django.contrib.auth.models import User
from django.test import TestCase
from signupapp.models import UserTable


# Create your tests here.
class LoginTest(TestCase):
    def setUp(self):
        self.userinfo1part1 = {'username': 'test1username',
                               'password': 'test1password',
                               'first_name': 'test1first_name',
                               'last_name': 'test1last_name',
                               'email': 'test1email@test.edu'}

        self.userinfo1part2 = {'university': 'ASU',
                               'isprofessor': 'True'}

        self.credentials1 = {'username': 'test1username',
                             'password': 'test1password',
                             'button_click': 'button_click'}

        UserTable.objects.create_user(user=User.objects.get(username='test1username'), **self.userinfo1part2)

        User.objects.create_user(**self.userinfo1part1)

        self.userinfo2part1 = {'username': 'test2username',
                               'password': 'test2password',
                               'first_name': 'test2first_name',
                               'last_name': 'test2last_name',
                               'email': 'test2email@test.edu'}

        self.userinfo2part2 = {'university': 'ASU',
                               'isprofessor': 'True'}

        self.credentials2 = {'username': 'test2username',
                             'password': 'test2password',
                             'button_click': 'button_click'}

        UserTable.objects.create_user(user=User.objects.get(username='test2username'), **self.userinfo2part2)

        User.objects.create_user(**self.userinfo2part1)
        self.userinfo3part1 = {'username': 'test3username',
                               'password': 'test3password',
                               'first_name': 'test3first_name',
                               'last_name': 'test3last_name',
                               'email': 'test3email@test.edu'}

        self.userinfo3part2 = {'university': 'ASU',
                               'isprofessor': 'True'}

        self.credentials3 = {'username': 'test3username',
                             'password': 'test3password',
                             'button_click': 'button_click'}

        UserTable.objects.create_user(user=User.objects.get(username='test3username'), **self.userinfo3part2)

        User.objects.create_user(**self.userinfo3part1)

        self.userinfo4part1 = {'username': 'test4username',
                               'password': 'test4password',
                               'first_name': 'test4first_name',
                               'last_name': 'test4last_name',
                               'email': 'test4email@test.edu'}

        self.userinfo4part2 = {'university': 'ASU',
                               'isprofessor': 'True'}

        self.credentials4 = {'username': 'test4username',
                             'password': 'test4password',
                             'button_click': 'button_click'}

        UserTable.objects.create_user(user=User.objects.get(username='test4username'), **self.userinfo4part2)

        User.objects.create_user(**self.userinfo4part1)

        self.userinfo5part1 = {'username': 'test5username',
                               'password': 'test5password',
                               'first_name': 'test5first_name',
                               'last_name': 'test5last_name',
                               'email': 'test5email@test.edu'}

        self.userinfo5part2 = {'university': 'ASU',
                               'isprofessor': 'True'}

        self.credentials5 = {'username': 'test5username',
                             'password': 'test5password',
                             'button_click': 'button_click'}

        UserTable.objects.create_user(user=User.objects.get(username='test5username'), **self.userinfo5part2)

        User.objects.create_user(**self.userinfo5part1)

        self.incorrect_credentials1 = {'username': 'test1username_incorrect',
                                       'password': 'test1password_incorrect',
                                       'button_click': 'button_click'}

        self.incorrect_credentials2 = {'username': 'test2username_incorrect',
                                       'password': 'test2password_incorrect',
                                       'button_click': 'button_click'}

        self.incorrect_credentials3 = {'username': 'test3username_incorrect',
                                       'password': 'test3password_incorrect',
                                       'button_click': 'button_click'}

        self.incorrect_credentials4 = {'username': 'test4username_incorrect',
                                       'password': 'test4password_incorrect',
                                       'button_click': 'button_click'}

        self.incorrect_credentials5 = {'username': 'test5username_incorrect',
                                       'password': 'test5password_incorrect',
                                       'button_click': 'button_click'}

    def test_correct_login(self):
        response = self.client.post('/login/', self.credentials1, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.client.logout()

        response = self.client.post('/login/', self.credentials2, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.client.logout()

        response = self.client.post('/login/', self.credentials3, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.client.logout()

        response = self.client.post('/login/', self.credentials4, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.client.logout()

        response = self.client.post('/login/', self.credentials5, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.client.logout()

    def test_incorrect_login(self):
        response = self.client.post(('/login/'), self.incorrect_credentials1, follow=False)
        self.assertFalse(True, response.read())

        response = self.client.post(('/login/'), self.incorrect_credentials2, follow=False)
        self.assertFalse(True, response.read())

        response = self.client.post(('/login/'), self.incorrect_credentials3, follow=False)
        self.assertFalse(True, response.read())

        response = self.client.post(('/login/'), self.incorrect_credentials4, follow=False)
        self.assertFalse(True, response.read())

        response = self.client.post(('/login/'), self.incorrect_credentials5, follow=False)
        self.assertFalse(True, response.read())
