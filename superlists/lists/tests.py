from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve

from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)

	def test_home_page_returns_correct_html(self):
		r = HttpRequest()
		res = home_page(r)
		self.assertTrue(res.content.startswith('<html>'))
		self.assertIn('<title>To-Do lists</title>', res.content)
		self.assertTrue(res.content.endswith('</html>'))
