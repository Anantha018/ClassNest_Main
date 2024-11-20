# classnest_Base/tests/test_integration.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from classnest_Base.models import Course

class QuizIntegrationTest(TestCase):

    def setUp(self):
        self.instructor = User.objects.create_user(
            username='testinstructor',
            email='instructor@example.com',
            password='password123'
        )
        self.course = Course.objects.create(
            title='Sample Course',
            description='This is a sample course.',
            instructor=self.instructor
        )

    def test_full_quiz_flow(self):
        with open('path/to/sample.pdf', 'rb') as pdf_file:
            response = self.client.post(reverse('upload_pdf'), {'pdf': pdf_file})
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('quiz_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Question")

        response = self.client.post(reverse('submit_quiz'), {'question_1': 'A', 'question_2': 'B'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your score")