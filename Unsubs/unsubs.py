from settings import *
from shared import *
import pandas as pd


def combine(df):
    df['ActiveUnsubs'] = df['Feedback Loop - ACTIVE'] + df['Feedback - ACTIVE'] + df['Web Site - ACTIVE'] + df['Android - ACTIVE']
    df['Other'] = df['Other'] + df['Postpone - NON-UNSUB'] + df['Website Update Email - NON-UNSUB']
    df['DeliveredMail'] = df['Messages Sent'] - df['Hard Bounce - INACTIVE']
    Metrics = df[['Beginning Subs', 'Ending Subs', 'DeliveredMail', 'Total Unsubs', 'Inactive Removal - INACTIVE', 'Hard Bounce - INACTIVE', 'ActiveUnsubs', 'Other']].sum()
    data = pd.DataFrame(Metrics)
    return data


def industry(df):
    data = df.groupby(['Primary Sub-category Category'])['Ending Subs'].sum()
    return data

if __name__ == '__main__':
    data = load(U)
    ad = sub_ad(data)
    ad_points = combine(ad)
    main_points = combine(data)
    data_summary = pd.DataFrame(concat([ad_points, main_points]))
    data_summary.columns = ['Ad Based','Total']
    data_industry = pd.DataFrame(industry(data))
    ad_industry = pd.DataFrame(industry(ad))
    industry_summary = concat([data_industry, ad_industry])
    # writer = ExcelWriter(SHEET_U_PROCESSED)
    data_summary.to_excel(writer, 'unsubs')
    industry_summary.to_excel(writer, 'industry', index = True)
    writer.save()
