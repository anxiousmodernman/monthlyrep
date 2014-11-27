__author__ = 'annaglander'

import sys
import argparse

from report.monthly import Unsubscribes, Opens, Profile

def do_monthly_reports(filename):
#class to complete reporting
    Opens = Opens(filename)
    # problem here is that the Opens class needs to deliver two tabs worth of information
    Unsubs = Unsubs(filename)
    Profile = Profile(filename)
    pass



class toExcel(object):
#class to write other classes to excel?
    def __init__(self, ):


    def save_xls(list_dfs, xls_path):
        writer = ExcelWriter(xls_path)
        for n, df in enumerate(list_dfs):
            df.to_excel(writer,'sheet%s' % n)
        writer.save()



