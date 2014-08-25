import unittest
from profile_completion import *
from globals import *

class ProfileCompletion(unittest.TestCase):

    def setUp(self):
        test_data = BASEPATH + FOLDER_PC + 'Profile Completeness_140703_test.xlsx'
        fields_data = FIELDS_PATH
        self.data = load_data(test_data, fields_data)

    def test_add_stats(self):
        tested = add_stats(self.data)
        test_val = tested[tested.Brief == 'AAAA']['TotalDataPoints']
        self.assertEqual(test_val.item(), 158217)
        pass

if __name__ == '__main__':
    unittest.main()
