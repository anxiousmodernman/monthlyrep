import datetime
from pandas import ExcelWriter

"""
Environment settings file.

Adjust USER to setup your environment variables.
"""

USER = 'Coleman'

print 'Environment settings loaded for %s' % USER


if USER == 'Anna':
    BASEPATH = 'C:\\Users\\anna\\Dropbox\\Product\\ALLTHEDATA\\'
    # BASEPATH = 'C:\\Users\\anna\\Desktop\\Code\\ALLTHEDATA\\'
    today = datetime.date.today()
    folder_processed = 'MonthlyRep'
    folder_date = str(today.year) + '_' + str(today.month)

    FOLDER_PC = 'Profile_completeness\\' + folder_date + '\\'
    SHEET_PC = 'Profile Completeness_14' + str(today.month) + '03.xls'
    SHEET_PC_PROCESSED = 'Profile Completeness_14' + str(today.month) + '03_processed.xls'
    FIELDS = 'Profile_completeness\\' + 'numfields_brief.xlsx'

    PC = BASEPATH + FOLDER_PC + SHEET_PC
    FIELDS_PATH = BASEPATH + FIELDS

    FOLDER_OC = 'Open_rates_clicks\\' + folder_date + '_opens_clicks\\'
    SHEET_OC = 'monthly_sent_open_click_report_14' + str(today.month) + '03.xls'
    SHEET_OC_PROCESSED = 'monthly_sent_open_click_report_14' + str(today.month) + '03_processed.xls'

    OC = BASEPATH + FOLDER_OC + SHEET_OC

    FOLDER_U= 'Unsubscribes_opt_outs\\' + folder_date + '\\'
    SHEET_U = 'monthly_unsub_dashboard_14' + str(today.month) + '03.xls'
    SHEET_U_PROCESSED = 'monthly_unsub_dashboard_14' + str(today.month) + '03_processed.xls'

    U = BASEPATH + FOLDER_U + SHEET_U

    writer = ExcelWriter(BASEPATH + folder_processed + folder_date + 'processed.xls')


if USER == 'Coleman':
    BASEPATH = 'C:\\Users\\anna\\Dropbox\\Product\\ALLTHEDATA\\'
    # BASEPATH = 'C:\\Users\\anna\\Desktop\\Code\\ALLTHEDATA\\'
    today = datetime.date.today()
    folder_processed = 'MonthlyRep'
    folder_date = str(today.year) + '_' + str(today.month)

    FOLDER_PC = 'Profile_completeness\\' + folder_date + '\\'
    SHEET_PC = 'Profile Completeness_14' + str(today.month) + '03.xls'
    SHEET_PC_PROCESSED = 'Profile Completeness_14' + str(today.month) + '03_processed.xls'
    FIELDS = 'Profile_completeness\\' + 'numfields_brief.xlsx'

    PC = BASEPATH + FOLDER_PC + SHEET_PC
    FIELDS_PATH = BASEPATH + FIELDS

    FOLDER_OC = 'Open_rates_clicks\\' + folder_date + '_opens_clicks\\'
    SHEET_OC = 'monthly_sent_open_click_report_14' + str(today.month) + '03.xls'
    SHEET_OC_PROCESSED = 'monthly_sent_open_click_report_14' + str(today.month) + '03_processed.xls'

    OC = BASEPATH + FOLDER_OC + SHEET_OC

    FOLDER_U= 'Unsubscribes_opt_outs\\' + folder_date + '\\'
    SHEET_U = 'monthly_unsub_dashboard_14' + str(today.month) + '03.xls'
    SHEET_U_PROCESSED = 'monthly_unsub_dashboard_14' + str(today.month) + '03_processed.xls'

    # U = BASEPATH + FOLDER_U + SHEET_U
    U = 'C:\\Users\\cmcfarland\\Dropbox\\Product\\ALLTHEDATA\\use_this\\monthly_unsub_dashboard_141103.xls'
    writer = ExcelWriter('C:\\Users\\cmcfarland\\Dropbox\\Product\\ALLTHEDATA\\use_this\\processed.xls')



