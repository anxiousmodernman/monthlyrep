__author__ = 'anna'

import unittest
from report.monthly import Opens
from settings import O


class OpensTest(unittest.TestCase):

    def setUp(self):
        self.test_report = Opens(O)

    def test_opens_by_category(self):
        internal_df = self.test_report._opens_by_category
        # Use the "at" method for accessing df cells via index + column
        # http://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-data-frame
        print internal_df

        value = internal_df.at['Sent', 'Total']
        self.assertEqual(value, 114318482)



if __name__ == '__main__':
    unittest.main()


