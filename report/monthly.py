import os
import pandas as pd
from shared import concat


class ReportBase(object):

    def __init__(self, file_input, sheet='Sheet1'):
        self._data = pd.read_excel(file_input, sheet=sheet)
        self.input_filename = file_input

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
        self._industry_subs = self._compute_subs_by_industry()
        self._unsubs_by_category = self._compute_unsubs_by_category()

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

    def _compute_subs_by_industry(self):
        # todo: put these column names in a dict of constants?
        industry_col = 'Primary Sub-category Category'
        subs_col = 'Ending Subs'
        # we can access self._data internally
        computed = self._data.groupby([industry_col])[subs_col].sum()
        return pd.DataFrame(computed)

    def _compute_unsubs_by_category(self):
        ad_based = self._subset_ad_based()
        all_briefs_summary = self._summarize_unsubs(self._data)
        ad_based_summary = self._summarize_unsubs(ad_based)
        combined = pd.DataFrame(concat([ad_based_summary, all_briefs_summary]))
        combined.columns = ['Ad Based', 'Total']
        return combined

    @staticmethod
    def _summarize_unsubs(df):

        df['ActiveUnsubs'] = \
            df['Feedback Loop - ACTIVE'] + \
            df['Feedback - ACTIVE'] + \
            df['Web Site - ACTIVE'] + \
            df['Android - ACTIVE']
        df['Other'] = \
            df['Other'] + \
            df['Postpone - NON-UNSUB'] + \
            df['Website Update Email - NON-UNSUB']
        df['DeliveredMail'] = df['Messages Sent'] - df['Hard Bounce - INACTIVE']

        cols = [
            'Beginning Subs',
            'Ending Subs',
            'DeliveredMail',
            'Total Unsubs',
            'Inactive Removal - INACTIVE',
            'Hard Bounce - INACTIVE',
            'ActiveUnsubs',
            'Other',
        ]
        metrics = df[cols].sum()
        summarized = pd.DataFrame(metrics)
        return summarized

    def render_excel(self, output_file):
        writer = pd.ExcelWriter(output_file)
        self._unsubs_by_category.to_excel(writer, 'unsubs')
        self._industry_subs.to_excel(writer, 'industry')
        print 'Writing output file to directory: %s' % os.path.abspath('.')
        writer.save()





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








