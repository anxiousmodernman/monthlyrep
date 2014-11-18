from settings import *
from shared import *
import pandas as pd


def combine(df):
    # create 'active unsubs' and 'other' column by summing other columns
    df['ActiveUnsubs'] = df['Feedback Loop - ACTIVE'] + df['Feedback - ACTIVE'] + df['Web Site - ACTIVE'] + df['Android - ACTIVE']
    df['Other'] = df['Other'] + df['Postpone - NON-UNSUB'] + df['Website Update Email - NON-UNSUB']
    # create 'delivered mail' column
    df['DeliveredMail'] = df['Messages Sent'] - df['Hard Bounce - INACTIVE']
<<<<<<< HEAD
    Metrics = df[['Beginning Subs', 'Ending Subs', 'DeliveredMail', 'Total unsubs', 'Inactive Removal - INACTIVE', 'Hard Bounce - INACTIVE', 'ActiveUnsubs', 'Other']].sum()
=======
    cols = ['Beginning Subs',
            'Ending Subs',
            'DeliveredMail',
            'Total Unsubs',
            'Inactive Removal - INACTIVE',
            'Hard Bounce - INACTIVE',
            'ActiveUnsubs',
            'Other',
            ]
    # create a Series object with labels
    Metrics = df[cols].sum()
    # convert Series to DataFrame
>>>>>>> eeba6c0bed58f3d75e6015f931eaa6fedd7b0194
    data = pd.DataFrame(Metrics)
    return data


def industry(df):
    data = df.groupby(['Primary Sub-category Category'])['Ending Subs'].sum()
    return data

if __name__ == '__main__':
    # load the data
    data = load(U)
    # subset Ad Based; fillna Brief Tags column
    ad = sub_ad(data)
    # summarize Ad Based stats
    ad_points = combine(ad)
    # summarize all brief stats
    main_points = combine(data)
    # join ad_points and main_points together by stacking cols next to each other
    data_summary = pd.DataFrame(concat([ad_points, main_points]))
    data_summary.columns = ['Ad Based', 'Total']

    # New sheet: sum subscribers by industry
    data_industry = pd.DataFrame(industry(data))
<<<<<<< HEAD
    ad_industry = pd.DataFrame(industry(ad))
    industry_summary = concat([data_industry, ad_industry])
=======

    # ad_industry = industry(ad)
    # industry_summary = concat([data_industry, ad_industry])
>>>>>>> eeba6c0bed58f3d75e6015f931eaa6fedd7b0194
    # writer = ExcelWriter(SHEET_U_PROCESSED)

    # write data to two excel sheets
    data_summary.to_excel(writer, 'unsubs')
    industry_summary.to_excel(writer, 'industry', index = True)
    writer.save()
