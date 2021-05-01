# get_data.py - Python script to fetch the data from the online spreadsheet
#               and save it as csv file
# 4/28/2021
#
# Meshal Albaiz

from gsheets import Sheets # get google sheets api library

def download_csv(): # method to fetch and download spreadsheet
    # get sheets using credentials
    sheets = Sheets.from_files('~\Desktop\OFB_Data\client_secrets.json', '~\Desktop\OFB_Data\storage.json')

    # set url to url of spreadsheet that contains survey entries
    url = 'https://docs.google.com/spreadsheets/d/1TgNM_HA6y2IMD6vEjxNqFzaUmfRtTMqsiHM7jK-16Kc/edit?usp=sharing'

    # get sheet
    s = sheets.get(url)

    # dump first sheet in spreadsheet into csv file
    s.sheets[0].to_csv('ofb_data.csv', encoding='utf-8', dialect='excel')
