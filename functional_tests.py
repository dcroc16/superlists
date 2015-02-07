import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
	def setup(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_creating_a_new_list(self):
		self.setup()
		# User Stories
		# Edith heard about a cool new online todo app, She goes
		# to check out its homepage

		self.browser.get('localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertEqual('To-Do',self.browser.title)
		
		# She is invited to enter a to-do item straight away
		self.tearDown()
		# She types "Buy Peacock Feathers" into a text box (Edith's Hoby)


if __name__ == '__main__':
	unittest.main()