import unittest
from report.monthly import Unsubscribes
from settings import U


class TestUnsubReport(unittest.TestCase):

    def setUp(self):
        """
        The setUp method is another part of the unittest framework.
        It will be run before the tests, and data set on "self" (the
        test instance) can be reused throughout the test. Here you
        do things like set up the environment. Similarly, there
        is also a tearDown method that can be run after all tests.
        """
        self.test_report = Unsubscribes(U)

    def test_create_unsub_report(self):
        """Prove that we can construct an instance of Unsubscribes"""
        self.assertIsInstance(self.test_report, Unsubscribes, msg="Should be an instance of class Unsubscribes")

    def test_total_unsubscribe_property(self):

        total_ad_based_unsubs = self.test_report.total_ad_based_unsubscribes
        self.assertEqual(total_ad_based_unsubs, 133301, msg="Should be equal")

    def test_beginning_subs_property(self):

        beginning_subs_ad_based = self.test_report.beginning_subs_ad_based
        self.assertEqual(beginning_subs_ad_based, 5103303, msg="Should be equal")

    def test_ad_based_sum(self):

        ad_based_sum = self.test_report.ad_based_sum('Beginning Subs')
        self.assertEqual(ad_based_sum, 5103303, msg="Should be equal")

    def test_compute_unsubs_by_category(self):

        internal_df = self.test_report._unsubs_by_category
        # Use the "at" method for accessing df cells via index + column
        # http://stackoverflow.com/questions/16729574/how-to-get-a-value-from-a-cell-of-a-data-frame
        value = internal_df.at['Ending Subs', 'Ad Based']
        self.assertEqual(value, 5122371)

    # def test_field_sum(self):
    #
    #     test_report = Unsubscribes(U)
    #     field_sum = test_report.field_sum(['Other','Postpone - NON-UNSUB','Website Update Email - NON-UNSUB'],'Other')
    #     field_sum._ad_based_sum
    #     self.assertEqual(field_sum, 5103303, msg="Should be equal")





if __name__ == '__main__':
    unittest.main()

