import pandas as pd


class Unsubscribes:
    """Class to represent data and computations for monthly unsubscribes report.
    """

    def __init__(self, file_input, sheet='Sheet1'):
        self._data = pd.read_excel(file_input, sheet=sheet)


