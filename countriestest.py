import application
import unittest

class TestCountriesCapitals(unittest.TestCase):

    def insert_country(self):
    #That is for check the user answer through raw_input
        self.assertEqual(application.insert_country("Paris"),True)
        self.assertEqual(application.insert_country(5),False)

#    def test_user_answer(self):
 #       self.assertEqual(application.user_answer(2),1)

if __name__ == '__main__':
    unittest.main()