# classnest_Base/tests/test_forms.py

from django.test import TestCase
from classnest_Base.forms import CourseForm

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