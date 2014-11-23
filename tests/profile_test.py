import unittest
from report.monthly import Profile
from settings import PC, FIELDS


class ProfileTest(unittest.TestCase):


    def setUp(self):
        self.test_report = Profile(PC, FIELDS)

    def test_create_profile(self):
        # every class that inherits from unittest must begin with test, and will be run
        #setup is unittest.test case method that is run pre all tests
        self.assertIsInstance(self.test_report, Profile)

    def test_compute_profile_attribute(self):
        internal_df = self.test_report._profile_by_category
        print internal_df
        value = internal_df.at['Subs with All', 'Ad Based']
        self.assertAlmostEqual(float(value), float(0.572455389054), msg="Should be equal")


if __name__ == '__main__':
    unittest.main()
