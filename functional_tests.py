import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
		header_text = self.browser.find_element_by_id('h1').text
		self.assertIn('To-Do',header_text)



		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
			)
		# She is invited to enter a to-do item straight away
		

		# She types "Buy Peacock Feathers" into a text box (Edith's Hoby)
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_id('tr')
		self.assertTrue(
				any(row.text == '1: Buy peacock feathers' for row in rows)
			)
		self.fail('Finish the test!')

		# There is still a text box inviting her to add another item
		# Edith wonders whether the site will remember her list.
		# Then she sees that the site has generated a unique URL for her ==
		# She visits that URL - her to-do list is still there.
		# satisfied she goes back to sleep

if __name__ == '__main__':
	unittest.main()