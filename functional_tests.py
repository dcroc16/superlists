import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
	def setup(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()

	def test_creating_a_new_list(self):
		self.setup()

		# User Stories
		# Edith heard about a cool new online todo app, She goes
		# to check out its homepage

		self.browser.get('localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertEqual('To-Do lists', self.browser.title)

		# She is invited to enter a to-do item straight away
		
		# She types "Buy Peacock Feathers" into a text box (Edith's Hoby)
		self.fail('Finish the test!')

		# There is still a text box inviting her to add another item
		# Edith wonders whether the site will remember her list.
		# Then she sees that the site has generated a unique URL for her ==
		# She visits that URL - her to-do list is still there.
		# satisfied she goes back to sleep

if __name__ == '__main__':
	unittest.main()