from django.test import TestCase
from signupapp.models import UserTable
from homeapp.models import PDF
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist


# Create your tests here.


class IndexTest(TestCase):
    def setUp(self):
        User.objects.create_user("Test1", email='test1@test.edu', password='test1password', first_name='Test',
                                 last_name='1')
        UserTable.objects.create(user=User.objects.get(username='Test1'), university="ASU", isprofessor=True)

        User.objects.create_user("Test2", email='test2@test.edu', password='test2password', first_name='Test',
                                 last_name='2')
        UserTable.objects.create(user=User.objects.get(username='Test2'), university="ASU", isprofessor=True)

        User.objects.create_user("Test3", email='test3@test.edu', password='test3password', first_name='Test',
                                 last_name='3')
        UserTable.objects.create(user=User.objects.get(username='Test3'), university="ASU", isprofessor=True)

        User.objects.create_user("Test4", email='test4@test.edu', password='test4password', first_name='Test',
                                 last_name='4')
        UserTable.objects.create(user=User.objects.get(username='Test4'), university="ASU", isprofessor=True)

        User.objects.create_user("Test5", email='test5@test.edu', password='test5password', first_name='Test',
                                 last_name='5')
        UserTable.objects.create(user=User.objects.get(username='Test5'), university="ASU", isprofessor=True)

    def test_check_this_works(self):
        c = Client()

        test1 = User.objects.get(username='Test1')
        self.assertEqual(test1.username, 'Test1')
        c.login(username='Test1', password='test1password')
        with open('homeapp/test/test1.pdf', encoding='latin-1') as fp:
            c.post('/homeapp/',
                   {'professor': 'Doc Brown', 'university': 'Hill Valley High School', 'subjectname': 'Time Travel',
                    'dropdown': 'Freshman', 'tag1': '88mph', 'tag2': 'Comedy', 'tag3': 'Physics', 'file_path': fp})

        pdf_test = PDF.objects.get(professor_name='Doc Brown')
        self.assertEqual(pdf_test.university, 'Hill Valley High School')

        c.post('/homeapp/editprofile',
               {'last_name': 'Who', 'first_name': 'Doctor', 'university': 'All of time and space',
                'isProfessor': 'checkedValue', 'old_password': 'test1password', 'new_password': 'Tardis1',
                'retype_new_password': 'Tardis1'})
        user_test = User.objects.get(username='Test1')
        self.assertTrue(user_test.first_name, 'Doctor')
        self.assertEqual(user_test.userinfo.university, 'All of time and space')
        c.logout()
        response = c.login(username='Test1', password='Tardis1')
        self.assertTrue(response)
        c.post('/homeapp/uploaded', {'Delete': pdf_test.id})
        self.assertRaises(PDF.DoesNotExist, PDF.objects.get, professor_name='Doc Brown')



        test2 = User.objects.get(username='Test2')
        self.assertEqual(test2.username, 'Test2')
        c.login(username='Test2', password='test2password')
        with open('homeapp/test/test1.pdf', encoding='latin-1') as fp:
            c.post('/homeapp/',
                   {'professor': 'Severus Snape', 'university': 'Hogwarts', 'subjectname': 'Potions',
                    'dropdown': 'Freshman', 'tag1': 'Biased', 'tag2': 'Slytherin', 'tag3': '', 'file_path': fp})

        response = c.post('/homeapp/uploaded')
        #print(response.context['List'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['List'], [[2, 'test1.pdf']])
        #self.assertContains(response, 'Company Name XYZ')


        test3 = User.objects.get(username='Test3')
        self.assertEqual(test3.username, 'Test3')

        test4 = User.objects.get(username='Test4')
        self.assertEqual(test4.username, 'Test4')

        test5 = User.objects.get(username='Test5')
        self.assertEqual(test5.username, 'Test5')
