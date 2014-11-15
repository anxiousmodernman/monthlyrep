import unittest
from report.monthly import Unsubscribes
from settings import U


class TestUnsubReport(unittest.TestCase):

    def test_create_unsub_report(self):
        """Prove that we can construct an instance of Unsubscribes"""
        test_report = Unsubscribes(U)

        # Here we are testing that test_report is an instance of class Unsubscribes
        self.assertIsInstance(test_report, Unsubscribes, msg="Should be an instance of class Unsubscribes")

    def test_total_unsubscribe_property(self):

        test_report = Unsubscribes(U)
        total_ad_based_unsubs = test_report.total_ad_based_unsubscribes
        self.assertEqual(total_ad_based_unsubs, 133301, msg="Should be equal")

    def test_beginning_subs_property(self):

        test_report = Unsubscribes(U)
        beginning_subs_ad_based = test_report.beginning_subs_ad_based
        self.assertEqual(beginning_subs_ad_based, 5103303, msg="Should be equal")

    def test_ad_based_sum(self):

        test_report = Unsubscribes(U)
        ad_based_sum = test_report.ad_based_sum('Beginning Subs')
        self.assertEqual(ad_based_sum, 5103303, msg="Should be equal")

    # def test_field_sum(self):
    #
    #     test_report = Unsubscribes(U)
    #     field_sum = test_report.field_sum(['Other','Postpone - NON-UNSUB','Website Update Email - NON-UNSUB'],'Other')
    #     field_sum._ad_based_sum
    #     self.assertEqual(field_sum, 5103303, msg="Should be equal")





if __name__ == '__main__':
    unittest.main()

