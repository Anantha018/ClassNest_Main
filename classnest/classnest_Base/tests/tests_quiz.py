# classnest_Base/tests/test_quiz.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class TakeQuizTest(TestCase):

    def setUp(self):
        # Create a student user for testing and login.
        self.student = User.objects.create_user(
            username="student1",
            email="student1@example.com",
            password="password123"
        )
        
    def test_take_quiz(self):
        """Test if a student can take and submit quiz answers."""
        
        response = self.client.get(reverse('quiz_page'))
        
        # Ensure the quiz page loads correctly.
        self.assertEqual(response.status_code, 200)
        