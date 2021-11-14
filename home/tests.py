from django.http import response
from django.test import TestCase,SimpleTestCase
from django.urls import reverse


# Create your tests here.
class HomeTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse("home")
        response=self.client.get(url)
        self.assertEqual(response,200)
    
    def test_about_us_page_status_code(self):
        url = reverse("about_us")
        response=self.client.get(url)
        self.assertEqual(response,200)

    def test_home_page_templet(self):
        url = reverse("home")
        response=self.client.get(url)
        self.assertTemplateUsed(response,"home.html")
    
    def test_about_us_page_templet(self):
        url = reverse("about_us")
        response=self.client.get(url)
        self.assertTemplateUsed(response,"aboutUs.html")