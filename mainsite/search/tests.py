from django.test import TestCase
from signupapp.models import UserTable
from homeapp.models import PDF
from django.test import Client
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
import json
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

    def test_check(self):
        c = Client()

        c.login(username='Test1', password='test1password')
        with open('homeapp/test/test1.pdf', encoding='latin-1') as fp:
            c.post('/homeapp/',
               {'professor': 'Doc Brown', 'university': 'Hill Valley High School', 'subjectname': 'Time Travel',
                'dropdown': 'Freshman', 'tag1': '88mph', 'tag2': 'Comedy', 'tag3': 'Physics', 'file_path': fp})


        response = c.get('/search/rest?format=json')
        json_data = json.loads(response.content)
        #print(dir(response))
        #print(response.content)
        print(json_data['results'])

        self.assertEqual(json_data['results'][0]['professor_name'], 'Doc Brown')

