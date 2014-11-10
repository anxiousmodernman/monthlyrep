import pandas as pd

def load(data_file):
    data = pd.read_excel(data_file, 'Sheet1')
    return data


def sub_ad(df):
    df['Brief Tags'] = df['Brief Tags'].fillna("Undefined")
    sub_ad = df[df['Brief Tags'].str.contains("(.*Ad Based.*|.*Voodoo Enabled.*)")]
    return sub_ad


def subset(df, column, text):
    subset = df[df[column].str.contains(text)]
    return subset


def less_subset(df, column, text):
    less_subset = df[~df[column].str.contains(text)]
    return less_subset


def concat(df_list):
    df = pd.concat(df_list, axis=1, ignore_index=False)
    return df


def concat_t(df_list):
    df = pd.concat(df_list, axis=0, ignore_index=False)
    return df