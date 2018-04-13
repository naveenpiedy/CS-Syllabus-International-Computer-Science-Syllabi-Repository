from django.test import TestCase
from signupapp.models import UserTable
from homeapp.models import PDF
from django.test import Client
from django.contrib.auth.models import User
from collections import Counter
from django.db.models import Count, Func, F
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
        PDF.objects.create(uploaders='Test1',university='ASU',pdfName='pdf1',professor_name='Prof.Chen',subjectName='SER518',
                           year='Senior',pdf_desc='desc1',pdf_topic='topic1',pdf_tags=['ta','ta','ta'])
        PDF.objects.create(uploaders='Test2', university='ASU', pdfName='pdf2', professor_name='Prof.Zhang',
                           subjectName='SER519',
                           year='Junior', pdf_desc='desc2', pdf_topic='topic2', pdf_tags=['ta2', 'ta2', 'ta2'])


    def test_check_this_works(self):
        c = Client()

        test1 = User.objects.get(username='Test1')
        self.assertEqual(test1.username, 'Test1')

        response=c.post('/stats/')
        self.assertEqual(response.context['piechart'].local_data, [3,3])


class IndexTest2(TestCase):
    def setUp(self):
        User.objects.create_user("Test1", email='test1@test.edu', password='test1password', first_name='Test',
                                 last_name='1')
        UserTable.objects.create(user=User.objects.get(username='Test1'), university="ASU", isprofessor=True)
        PDF.objects.create(uploaders='Test1', university='ASU', pdfName='pdf1', professor_name='Prof.Chen',
                           subjectName='SER518',year='Senior', pdf_desc='desc1', pdf_topic='topic1', pdf_tags=['Computing Theory'])
        PDF.objects.create(uploaders='Test2', university='ASU', pdfName='pdf2', professor_name='Prof.Zhang',
                           subjectName='SER519',year='Junior', pdf_desc='desc2', pdf_topic='topic2', pdf_tags=['Software Engineering'])



    def test_check_this_works(self):
        c = Client()
        test1 = User.objects.get(username='Test1')
        self.assertEqual(test1.username, 'Test1')
        response = c.post('/stats/analyze',{'year':'Junior'})
        self.assertEqual(response.context['piechart'].local_data, [1])

class IndexTest3(TestCase):
    def setUp(self):
        User.objects.create_user("Test1", email='test1@test.edu', password='test1password', first_name='Test',
                                 last_name='1')
        UserTable.objects.create(user=User.objects.get(username='Test1'), university="ASU", isprofessor=True)
        PDF.objects.create(uploaders='Test1', university='ASU', pdfName='pdf1', professor_name='Prof.Chen',
                           subjectName='SER518',year='Senior', pdf_desc='desc1', pdf_topic='topic1', pdf_tags=['Software Engineering'])
        PDF.objects.create(uploaders='Test2', university='ASU', pdfName='pdf2', professor_name='Prof.Zhang',
                           subjectName='SER519',year='Junior', pdf_desc='desc2', pdf_topic='topic2', pdf_tags=['Software Engineering'])
        PDF.objects.create(uploaders='Test1', university='OSU', pdfName='pdf2', professor_name='Prof.Zhang',
                           subjectName='SER519', year='Junior', pdf_desc='desc2', pdf_topic='topic2',
                           pdf_tags=['Software Engineering'])
        PDF.objects.create(uploaders='Test2', university='NCSU', pdfName='pdf2', professor_name='Prof.Zhang',
                           subjectName='SER519', year='Junior', pdf_desc='desc2', pdf_topic='topic2',
                           pdf_tags=['Software Engineering'])
        PDF.objects.create(uploaders='Test2', university='NCSU', pdfName='pdf2', professor_name='Prof.Zhang',
                           subjectName='SER519', year='Junior', pdf_desc='desc2', pdf_topic='topic2',
                           pdf_tags=['Software Engineering'])
        PDF.objects.create(uploaders='Test2', university='Harvard', pdfName='pdf2', professor_name='Prof.Zhang',
                           subjectName='SER519', year='Junior', pdf_desc='desc2', pdf_topic='topic2',
                           pdf_tags=['Software Engineering'])
        PDF.objects.create(uploaders='Test2', university='MIT', pdfName='pdf2', professor_name='Prof.Zhang',
                           subjectName='SER519', year='Junior', pdf_desc='desc2', pdf_topic='topic2',
                           pdf_tags=['Software Engineering'])




    def test_check_this_works(self):
        c = Client()
        test1 = User.objects.get(username='Test1')
        self.assertEqual(test1.username, 'Test1')
        response = c.post('/stats/university', {'tag': 'Software Engineering'})
        self.assertEqual(response.context['piechart'].local_data, [2,1,2,1,1])