import pandas as pd


class Unsubscribes:
    """Class to represent data and computations for monthly unsubscribes report.
    """

    def __init__(self, file_input, sheet='Sheet1'):
        self._data = pd.read_excel(file_input, sheet=sheet)

    @property
    def my_property(self):
        something = 'Hello'
        return something

    @property
    def total_unsubscribes(self):
        pass

    @property
    def total_ad_based_unsubscribes(self):
        subsetted = self._subset_ad_based()
        return subsetted['Total Unsubs'].sum()

    def _subset_ad_based(self):
        ad_based = self._data
        ad_based['Brief Tags'] = ad_based['Brief Tags'].fillna(value="Undefined")
        ad_based = self._data[self._data['Brief Tags'].str.contains("(.*Ad Based.*|.*Voodoo Enabled.*)")]
        return ad_based



