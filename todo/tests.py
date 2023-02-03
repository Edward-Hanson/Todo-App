from django.test import TestCase, SimpleTestCase
from .models import Todo
from django.contrib.auth import get_user_model

# Create your tests here.
class TodoTests(SimpleTestCase):
    
    def setUp(self):
        
        user= get_user_model().objects.create_user(username='Eddy',email='eddy@gmail.com',age=12, password='test123')
        todo= Todo.objects.create(task= 'Play with Django', author=self.user)