from django.test import TestCase
from signupapp.models import UserTable
from homeapp.models import PDF
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



# Create your tests here.
class IndexTest1(TestCase):
    def setUp(self):
        User.objects.create_user("Test1", email='test1@test.edu', password='test1password', first_name='Test',
                                 last_name='1')
        UserTable.objects.create(user=User.objects.get(username='Test1'), university="ASU", isprofessor=True)

        User.objects.create_user("Test2", email='test2@test.edu', password='test2password', first_name='Test',
                                 last_name='2')
        UserTable.objects.create(user=User.objects.get(username='Test2'), university="ASU", isprofessor=True)



    def test_check_this_works(self):
        c = Client()

        test1 = User.objects.get(username='Test1')
        self.assertEqual(test1.username, 'Test1')
        c.login(username='Test1', password='test1password')
        c.post('/stats/')

        # with open('homeapp/test/test1.pdf', encoding='latin-1') as fp:
        #     c.post('/homeapp/',
        #         {'professor': 'Doc Brown', 'university': 'Hill Valley High School', 'subjectname': 'Time Travel',
        #             'dropdown': 'Freshman', 'tag1': '88mph', 'tag2': 'Comedy', 'tag3': 'Physics', 'file_path': fp})
        #
        # pdf_test = PDF.objects.get(professor_name='Doc Brown')
        # self.assertEqual(pdf_test.university, 'Hill Valley High School')
        #
        # test2 = User.objects.get(username='Test2')
        # self.assertEqual(test2.username, 'Test2')
