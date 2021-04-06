from django.test import TestCase
from film_site.models import Category
from django.urls import reverse

# Create your tests here.
class CategoryMethodTests(TestCase):

    def test_ensure_category_exist(self):
        #Check if the categories existing work
        category = Category(category=6)
        category.save()
    
        self.assertEqual(category.category==6,True)


    def test_slug_line_creation(self):
        #Check that the slug is created correctly
        category = Category(category=1)
        category.save()
        self.assertEqual(category.slug, '1')


class ViewTests(TestCase):
    
    def certain_film_test_no_review(self):
        #Check that a certain film has no reviews
        response = self.client.get(reverse('film_site:film'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No reviews for this film yet.')
    
    
