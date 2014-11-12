import pandas as pd
from settings import *
from shared import *


def load_data(data_file, fields_file):
    data = pd.read_excel(data_file, 'Sheet1')
    fields = pd.read_excel(fields_file, 'Sheet1')
    df = data[['Brief', 'Brief Tags', 'Total Subs', 'Subs with NO norm data', 'Subs with one field', 'Subs with two fields', 'Subs with three fields', 'Subs with four fields', 'Subs with ALL norm data']]
    df_new = pd.merge(df, fields, left_on='Brief', right_on='Brief', how='left')
    return df_new


def check_fields(df):
    field_null = df[df['NumFields'].isnull()]
    if len(field_null) > 0:
        print field_null.Brief
    else:
        print 'no new briefs'


def add_stats(df):
    df['denom'] = df.NumFields * df["Total Subs"]
    df['TotalDataPoints'] = df["Subs with one field"] + df["Subs with two fields"] * 2 + df["Subs with three fields"] * 3 + df["Subs with four fields"] * 4 + df["Subs with ALL norm data"] * 5
    return df


def total_subs_with_all(df):
    ref = df.columns.get_loc("Subs with NO norm data")
    df['NumFields_I'] = df['NumFields'].astype(int)
    df['ALLSUBSALL'] = df.apply(lambda r: r[ref + r['NumFields_I']:ref + 6].sum(), axis=1) # for every row
    # find starting row (ref) and add the number of fields to it, then sum the difference from ref + 6
    return df



def sum_stats(df, text):
    subs_all = float(df["ALLSUBSALL"].sum())/df["Total Subs"].sum()
    profile_completion = float(df['TotalDataPoints'].sum())/df["denom"].sum()
    return pd.Series([subs_all, profile_completion], index=['Subs with All', 'Profile Completion'], name=text)



if __name__ == '__main__':
    data = load_data(PC, FIELDS_PATH)
    check_fields(data)
    data = add_stats(data)
    data = total_subs_with_all(data)
    sub_ad = sub_ad(data)
    # sub_ed = subset(data, 'Primary Sub-category Category', "Education")
    # sub_hc = subset(data, 'Primary Sub-category Category', "Health Care")
    # sub_ad_less = less_subset(sub_ad, 'Primary Sub-category Category', "(Health Care|Education)")
    tot = sum_stats(data, 'tot')
    ad = sum_stats(sub_ad, 'ad')
    # ed = sum_stats(sub_ed, 'ed')
    # hc = sum_stats(sub_hc, 'hc')
    # ad_less = sum_stats(sub_ad_less, 'ad_less')
    df = concat([tot, ad])
    df.to_excel(writer, sheet_name='datacompletion', index=True)
    writer.save()







