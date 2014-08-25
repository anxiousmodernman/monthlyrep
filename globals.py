__author__ = 'anna'

import datetime

BASEPATH = 'C:\\Users\\anna\\Desktop\\Code\\ALLTHEDATA\\Profile_completeness\\'
today = datetime.date.today()

FOLDER_PC = str(today.year) + '_' + '0' + str(today.month-2) + '\\'
SHEET = 'Profile Completeness_140' + str(today.month-1) + '03.xls'
FIELDS = 'numfields_brief.xlsx'

PC = BASEPATH + FOLDER_PC + SHEET
FIELDS_PATH = BASEPATH + FIELDS