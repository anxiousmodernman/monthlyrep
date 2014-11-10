from globals import *
from shared import *
import pandas as pd


def main(df):
    main = df[df['Brief'] == df['Parent Brief']]
    return main


def nonmain(df):
    nonmain = df[df['Brief'] != df['Parent Brief']]
    return nonmain


def rates(df):
    OpenRate = float(df['Opens'].sum())/df['Sent'].sum()
    ClickRate = float(df['Clicks'].sum())/df['Opens'].sum()
    Metrics = df[['Sent', 'Opens', 'Clicks', 'Starting Subs', 'Ending Subs']].sum()
    data = pd.Series(Metrics).append(pd.Series([OpenRate, ClickRate]))
    data = pd.DataFrame(data)
    return data




if __name__ == '__main__':
    data = load(OC)
    main = main(data)
    ad = sub_ad(main)
    # nonmain = nonmain(data)
    # sr = subset(nonmain, 'Brief', ".*SR$")
    # ds = subset(nonmain, 'Brief', "DedicatedSend")
    # sf = subset(nonmain, 'Brief', "Sponsored_Feature")
    # trials = less_subset(nonmain, 'Brief', ".*SR$|Dedicated Send|Sponsored_Feature")
    ad_points = rates(ad)
    main_points = rates(main)
    # sr_points = rates(sr)
    # ds_points = rates(ds)
    # trials_points = rates(trials)
    # data = concat([ad_points, main_points, sr_points, ds_points, trials_points])
    data = concat([ad_points, main_points])
    data.columns = ['Ad Based','Total']
    data.to_excel(writer, 'openclick', index=True)
    writer.save()