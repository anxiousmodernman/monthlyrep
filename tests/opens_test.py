__author__ = 'anna'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


class TestUnsubReport(unittest.TestCase):

    def setUp(self):
        """
        The setUp method is another part of the unittest framework.
        It will be run before the tests, and data set on "self" (the
        test instance) can be reused throughout the test. Here you
        do things like set up the environment. Similarly, there
        is also a tearDown method that can be run after all tests.
        """
        self.test_report = Opens(O)

    def test_create_opens_report(self):
        """Prove that we can construct an instance of Unsubscribes"""
        self.assertIsInstance(self.test_report, Opens, msg="Should be an instance of class Opens")


    def test_opens_by_category(self):
        internal_df = self.test_report._opens_by_category
        # Use the "at" method for accessing df cells via index + column
        # http://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-data-frame
        value = internal_df.at['Ending Subs', 'Ad Based']
        self.assertEqual(value, 5122371)



if __name__ == '__main__':
    unittest.main()
