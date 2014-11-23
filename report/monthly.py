import os
import pandas as pd
from shared import concat


class ReportBase(object):

    def __init__(self, file_input, sheet='Sheet1'):
        self._data = pd.read_excel(file_input, sheet=sheet)
        self.input_filename = file_input

    def _subset_ad_based(self):
        #instance variable, of instance method
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

#todo: MAKE THIS WORK. :)
    def render_excel(self, output_file):
        writer = pd.ExcelWriter(output_file)
        self._unsubs_by_category.to_excel(writer, 'unsubs')
        self._industry_subs.to_excel(writer, 'industry')
        print 'Writing output file to directory: %s' % os.path.abspath('.')
        writer.save()
    #dont need an instance to call a static method
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


# I followed your example here, but things still arent lining up and its not 'easy to test' as you say it should be
class Opens(ReportBase):
    """Class to represent data and computations for monthly open click report.
    """

    def __init__(self, file_input, sheet='Sheet1'):
        super(Opens, self).__init__(file_input, sheet)
        self.data = self._subset_main()
        self._opens_by_category = self._compute_opens_by_category()
#todo: find out if main function is creating test discrepcancy
    def _subset_main(self):
        main = self._data[self._data['Brief'] == self._data['Parent Brief']]
        return main

    def _compute_opens_by_category(self):
        ad_based = self._subset_ad_based()
        main_briefs_summary = self._summarize_opens(self._data)
        ad_based_summary = self._summarize_opens(ad_based)
        combined = pd.DataFrame(concat([ad_based_summary, main_briefs_summary]))
        combined.columns = ['Ad Based', 'Total']

        return combined

    def render_excel(self, output_file):
        writer = pd.ExcelWriter(output_file)
        self._opens_to_category.to_excel(writer, 'opens')
        print 'Writing output file to directory: %s' % os.path.abspath('.')
        writer.save()


    @staticmethod
    def _summarize_opens(df):

        cols = [
            'Sent',
            'Opens',
            'Clicks',
            'Starting Subs',
            'Ending Subs',
        ]
        metrics = df[cols].sum()
        open_rate = float(df['Opens'].sum())/df['Sent'].sum()
        click_rate = float(df['Clicks'].sum())/df['Opens'].sum()
        summary = pd.Series(metrics).append(pd.Series([open_rate, click_rate]))
        summarized = pd.DataFrame(summary)

        return summarized


class Profile(ReportBase):
    """Class to represent data and computations for monthly profile completion numbers.
    """

    def __init__(self, file_input, fields_file, sheet='Sheet1'):
        super(Profile, self).__init__(file_input, sheet)
        #DROP DEBUGGER
        # import pdb
        # pdb.set_trace()
        self._num_fields_present = pd.read_excel(fields_file)
        self._data = self._build_profile_data()
        self._profile_by_category = self._compute_profile_by_category()

    def _build_profile_data(self):
        return self._join_fields(self._num_fields_present)

    def _join_fields(self, fields):

        df_new = pd.merge(self._data, fields, left_on='Brief', right_on='Brief', how='left')
        field_null = fields[fields['NumFields'].isnull()]
        if len(field_null) > 0:
            print field_null.Brief
            raise Exception('new briefs required')
        else:
            return df_new

    def _compute_profile_by_category(self):

        ad_based = self._subset_ad_based()
        all_briefs_summary = self._summarize_profile(self._data)
        ad_based_summary = self._summarize_profile(ad_based)
        combined = pd.DataFrame(concat([ad_based_summary, all_briefs_summary]))
        combined.columns = ['Ad Based', 'Total']

        return combined


    @staticmethod
    def _total_subs_with_all(df):
        ref = df.columns.get_loc("Subs with NO norm data")
        df['NumFields_I'] = df['NumFields'].astype(int)
        df['ALLSUBSALL'] = df.apply(lambda r: r[ref + r['NumFields_I']:ref + 6].sum(), axis=1) # for every row
        # find starting row (ref) and add the number of fields to it, then sum the difference from ref + 6
        total_subs_with_all = df['ALLSUBSALL'].sum()
        return total_subs_with_all


    @staticmethod
    def _total_possible_points(df):
        df['total_possible_points'] = df.NumFields * df["Total Subs"]
        total_possible_points = df['total_possible_points'].sum()
        return total_possible_points


    @staticmethod
    def _total_data_points(df):
        df['TotalDataPoints'] = df["Subs with one field"] + df["Subs with two fields"] * 2 + df["Subs with three fields"] * 3 + df["Subs with four fields"] * 4 + df["Subs with ALL norm data"] * 5
        total_data_points = df['TotalDataPoints'].sum()
        return total_data_points


    @staticmethod
    def _total_subs(df):
        total_subs = df['Total Subs'].sum()
        return total_subs



    def _summarize_profile(self, df):

        subs_all = self._total_subs_with_all(df)/float(self._total_subs(df))
        profile_completion = self._total_data_points(df)/float(self._total_possible_points(df))
        summarized = pd.Series([subs_all, profile_completion], index=['Subs with All', 'Profile Completion'])

        return summarized

    def render_excel(self, output_file):
        writer = pd.ExcelWriter(output_file)
        self._profile_by_category.to_excel(writer, 'opens')
        print 'Writing output file to directory: %s' % os.path.abspath('.')
        writer.save()




