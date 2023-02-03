from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


# Create your tests here.
class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User= get_user_model()
        user= User.objects.create_user(
            username='Eddy',
            email='eddy@gmail.com',
            age=12,
            password='test123'
            )
        self.assertEqual(user.username,'Eddy')
        self.assertEqual(user.email,'eddy@gmail.com')
        self.assertEqual(user.age,12)
        
class SignupPageTests(TestCase):
    
    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        
    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')
