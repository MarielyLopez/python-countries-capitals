import application
import unittest

class TestCountriesCapitals(unittest.TestCase):

    def testinsert_country(self):
    #That is for check the user answer through raw_input

    def testoption_user(self):
        self.assertEqual(application.option_user(),"1")

    def testclear(self):
        self.assertEqual(application.clear(),True)


    def testverific_country_and_capital(self):
       # self.assertEqual(application.verific_country_and_capital("sad"), True)
        self.assertTrue(application.verific_country_and_capital("sad"))


#    def test_user_answer(self):
 #       self.assertEqual(application.user_answer(2),1)

if __name__ == '__main__':
    unittest.main()
