import pandas as pd


class ReportBase(object):

    def __init__(self, file_input, sheet='Sheet1'):
        self._data = pd.read_excel(file_input, sheet=sheet)

    def _subset_ad_based(self):
        data = self._data
        data['Brief Tags'] = data['Brief Tags'].fillna(value="Undefined")
        ad_based = self._data[self._data['Brief Tags'].str.contains("(.*Ad Based.*|.*Voodoo Enabled.*)")]
        return ad_based


class Unsubscribes(ReportBase):
    """Class to represent data and computations for monthly unsubscribes report.
    """

    def __init__(self, file_input, sheet='Sheet1'):
        super(Unsubscribes, self).__init__(file_input, sheet)

    @property
    def total_unsubscribes(self):
        pass


    @property
    def total_ad_based_unsubscribes(self):
        subsetted = self._subset_ad_based()
        return subsetted['Total Unsubs'].sum()


    @property
    def beginning_subs_ad_based(self):
        ad = self._subset_ad_based()
        bs = ad['Beginning Subs'].sum()
        return bs


    def ad_based_sum(self, name):
        ad = self._subset_ad_based()
        bs = ad[name].sum()
        return bs

    # def field_sum(self, names, new_name):
    #     for i in names
    #
    #     return

    #
    # def _industry(self):
    #     data = self._data
    #     ad_based = total_ad_based_unsubscribes(data)
    #     industry = ad_based.groupby(['Primary Sub-category Category'])['Ending Subs'].sum()
    #     return industry

# def combine(df):
#     df['ActiveUnsubs'] = df['Feedback Loop - ACTIVE'] + df['Feedback - ACTIVE'] + df['Web Site - ACTIVE'] + df['Android - ACTIVE']
#     df['Other'] = df['Other'] + df['Postpone - NON-UNSUB'] + df['Website Update Email - NON-UNSUB']
#     df['DeliveredMail'] = df['Messages Sent'] - df['Hard Bounce - INACTIVE']
#     Metrics = df[['Beginning Subs', 'Ending Subs', 'DeliveredMail', 'Total Unsubs', 'Inactive Removal - INACTIVE', 'Hard Bounce - INACTIVE', 'ActiveUnsubs', 'Other']].sum()
#     data = pd.DataFrame(Metrics)
#     return data






