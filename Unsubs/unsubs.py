from globals import *
from shared import *
import pandas as pd


def combine(df):
    df['ActiveUnsubs'] = df['Feedback Loop - ACTIVE'] + df['Feedback - ACTIVE'] + df['Web Site - ACTIVE'] + df['Android - ACTIVE']
    df['Other'] = df['Other'] + df['Postpone - NON-UNSUB'] + df['Website Update Email - NON-UNSUB']
    df['DeliveredMail'] = df['Messages Sent'] - df['Hard Bounce - INACTIVE']
    Metrics = df[['Starting Subs', 'Ending Subs', 'DeliveredMail', 'Total Unsubs', 'Inactive Removal - INACTIVE', 'Hard Bounce - INACTIVE', 'ActiveUnsubs', 'Other']]
    data = pd.DataFrame(Metrics).T
    return data

def industry(df):
    data = df.groupby(['Primary Sub-category Category'])['Ending Subs'].sum()
    return data

if __name__ == '__main__':
    data = load(OC)
    ad = sub_ad(data)
    ad_points = combine(ad)
    main_points = combine(data)
    data = concat([ad_points, main_points])
    data_industry = industry(data)
    data.to_excel(SHEET_U_PROCESSED, sheet_name='sheet1', index=False)
    data_industry.to_excel(SHEET_U_PROCESSED, sheet_name= 'sheet1', index= False)