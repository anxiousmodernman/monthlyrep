import unittest
from report.monthly import *
from settings import O, U, PC, FIELDS


class CombinedReportTest(unittest.TestCase):

    def setUp(self):
        open_rep = Opens(O)
        unsubs = Unsubscribes(U)
        profile_comp = Profile(PC, FIELDS)
        self.combined_report = CombinedReportWriter(unsub=unsubs, opens=open_rep, profile=profile_comp)

    def test_create_instance_of_combined_report(self):
        self.assertIsInstance(self.combined_report, CombinedReportWriter)

    def test_write_excel(self):
        self.combined_report.save_xls(path='test_file.xls')
        self.assertTrue(os.path.exists('test_file.xls'))
        os.remove('test_file.xls')



