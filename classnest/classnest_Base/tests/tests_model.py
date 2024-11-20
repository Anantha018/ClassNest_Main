# classnest_Base/tests/test_models.py

from django.test import TestCase
from django.contrib.auth.models import User
from classnest_Base.models import Course
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

class QuizModelTest(TestCase):

    def setUp(self):
        self.student = User.objects.create_user(
            username='teststudent',
            email='student@example.com',
            password='password123'
        )
        self.quiz = Quiz.objects.create(
            title='Sample Quiz',
            description='This is a sample quiz.',
            created_by=self.student
        )

    def test_quiz_creation(self):
        self.assertEqual(self.quiz.title, 'Sample Quiz')
        self.assertEqual(self.quiz.description, 'This is a sample quiz.')
        self.assertEqual(self.quiz.created_by.username, 'teststudent')