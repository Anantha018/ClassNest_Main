from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from classnest_Base.models import Course
from classnest_Base.forms import CourseForm  # Ensure this import is correct
#from quiz_app.models import Quiz  # Update this import if Quiz is in a different app

class CourseModelTest(TestCase):

    def setUp(self):
        self.instructor = User.objects.create_user(
            username='testinstructor',
            email='instructor@example.com',
            password='password123'
        )
        self.course = Course.objects.create(
            title='Test Course',
            description='This is a test course.',
            instructor=self.instructor
        )

    def test_course_title(self):
        self.assertEqual(self.course.title, 'Test Course')

    def test_course_description(self):
        self.assertEqual(self.course.description, 'This is a test course.')

    def test_course_instructor(self):
        self.assertEqual(self.course.instructor.username, 'testinstructor')

# class QuizModelTest(TestCase):

#     def setUp(self):
#         self.student = User.objects.create_user(
#             username='teststudent',
#             email='student@example.com',
#             password='password123'
#         )
#         self.quiz = Quiz.objects.create(
#             title='Sample Quiz',
#             description='This is a sample quiz.',
#             created_by=self.student
#         )

#     def test_quiz_creation(self):
#         self.assertEqual(self.quiz.title, 'Sample Quiz')
#         self.assertEqual(self.quiz.description, 'This is a sample quiz.')
#         self.assertEqual(self.quiz.created_by.username, 'teststudent')

# class UploadPDFViewTest(TestCase):

#     def setUp(self):
#         self.instructor = User.objects.create_user(
#             username='testinstructor',
#             email='instructor@example.com',
#             password='password123'
#         )
#         self.client.login(username='testinstructor', password='password123')

#     def test_upload_pdf_view_get(self):
#         response = self.client.get(reverse('upload_pdf'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'Quiz_Base/upload.html')

#     def test_upload_pdf_view_post(self):
#         with open('path/to/sample.pdf', 'rb') as pdf_file:
#             response = self.client.post(reverse('upload_pdf'), {'pdf': pdf_file})
#         self.assertEqual(response.status_code, 200)

class CourseFormTest(TestCase):

    def test_valid_course_form(self):
        form_data = {
            'title': 'New Course',
            'description': 'This is a new course.'
        }
        form = CourseForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_course_form(self):
        form_data = {
            'title': '',
            'description': 'This is an incomplete course.'
        }
        form = CourseForm(data=form_data)
        self.assertFalse(form.is_valid())

# class QuizIntegrationTest(TestCase):

#     def setUp(self):
#         self.instructor = User.objects.create_user(
#             username='testinstructor',
#             email='instructor@example.com',
#             password='password123'
#         )
#         self.course = Course.objects.create(
#             title='Sample Course',
#             description='This is a sample course.',
#             instructor=self.instructor
#         )

#     def test_full_quiz_flow(self):
#         with open('path/to/sample.pdf', 'rb') as pdf_file:
#             response = self.client.post(reverse('upload_pdf'), {'pdf': pdf_file})
#         self.assertEqual(response.status_code, 200)

#         response = self.client.get(reverse('quiz_page'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Question")

#         response = self.client.post(reverse('submit_quiz'), {'question_1': 'A', 'question_2': 'B'})
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Your score")