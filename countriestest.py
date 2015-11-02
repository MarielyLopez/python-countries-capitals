import application
import unittest

class TestCountriesCapitals(unittest.TestCase):
	
	def test_verific_country_and_capital(self):
		self.assertEqual(application.verific_country_and_capital("sad"), True)

	def test_clear(self):
		self.assertEqual(application.clear(),True)

	def test_ingresa(self):
		self.assertEqual(application.check("yes"),False)
		self.assertTrue(application.check("no"),True)

	def test_check(self):
		self.assertFalse(application.check("yes"),False)
		self.assertTrue(application.check("no"),True)


if __name__ == '__main__':
    unittest.main()



