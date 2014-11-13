import unittest
from report.monthly import Unsubscribes
from settings import U


class TestUnsubReport(unittest.TestCase):

    def test_create_unsub_report(self):
        """Prove that we can construct an instance of Unsubscribes"""
        test_report = Unsubscribes(U)

        # Here we are testing that test_report is an instance of class Unsubscribes
        self.assertIsInstance(test_report, Unsubscribes, msg="Should be an instance of class Unsubscribes")
