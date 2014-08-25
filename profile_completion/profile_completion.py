import pandas as pd
from globals import *


def load_data(data_file, fields_file):
    data = pd.read_excel(data_file, 'Sheet1')
    fields = pd.read_excel(fields_file, 'Sheet1')
    data = pd.merge(data, fields, left_on='Brief', right_on='Brief', how='left')
    return data


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
    df['ALLSUBSALL'] = df.apply(lambda r: r[ref + r['NumFields']:ref + 6].sum(), axis=1) # for every row
    # find starting row (ref) and add the number of fields to it, then sum the difference from ref + 6
    return df


def sum_stats(df):
    subs_all = df["TotalSubs"].sum() / df["ALLSUBSALL"].sum()
    profile_completion = df['TotalDataPoints'].sum()/df["denom"].sum()
    return c(subs_all, profile_completion)


def subset_briefs(df):
    df['Brief Tags'] = df['Brief Tags'].fillna("Undefined")
    sub_ad = df[df['Brief Tags'].str.contains("(.*Ad Based.*|.*Voodoo.*)")]
    sub_ed = df[df['Primary Sub-category Category'].str.contains("Education")]
    sub_hc = df[df['Primary Sub-category Category'].str.contains("Health Care")]
    sub_ad_less = sub_ad[~sub_ad['Primary Sub-category Category'].str.contains("(Health Care|Education)")]
    return sub_ad, sub_ed, sub_hc, sub_ad_less


if __name__ == '__main__':
    data = load_data(PC, FIELDS_PATH)
    check_fields(data)
    data = add_stats(data)




