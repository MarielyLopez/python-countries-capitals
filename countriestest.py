import application
import unittest

class TestCountriesCapitals(unittest.TestCase):

    def test_clear(self):
        self.assertEqual(application.clear(),True)


    def test_verific_country_and_capital(self):
        self.assertEqual(application.verific_country_and_capital("sad"), True)
        #self.assertTrue(application.verific_country_and_capital("sad"))

def test_check(self):
    sel assertFalse(application.check("y"))

#    def test_user_answer(self):
 #       self.assertEqual(application.user_answer(2),1)

if __name__ == '__main__':
    unittest.main()