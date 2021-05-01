# process_data.py - Python script to process the data and save it in lists
# 4/28/2021
#
# Meshal Albaiz

import numpy as np
import csv
from indices import *
from zipcode_class import Zipcode

entries = [] # list of entries (list of lists)
zipcodes = [] # list of zipcode objects
questions = [] # list of questions

def open_csv(): # open csv file and populate lists, create zipcode objects
    with open('ofb_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader: # for each line
            if line_count == 0: # for first line
                for question in row: # save questions to question array
                    questions.append(question)
                line_count += 1 # increment line count
            else: # for lines after the first line
                entries.append(row) # save entry to entries list
                line_count += 1 # increment line count
        print(f'Processed {line_count-1} entries.') # print how many entries were processed

def process_entries(): # process entries by creating/updating zipcode objects
    for entry in entries: # for each entry
        zipcode = entry[zipcode_index] # get zipcode
        exists = False # zipcode assumed new iniatially

        if(len(zipcodes) == 0): # if zipcodes list is empty
            new_zipcode = Zipcode(entry) # create new zipcode object
            zipcodes.append(new_zipcode) # append to list of zipcodes

        else: # if zipcodes list is not empty
            for item in zipcodes: # for each zipcode
                if(zipcode == item.zipcode): # if zipcode exists
                    exists = True # mark it existing
                    item.update_values(entry) # update existing zipcode with entry
                    break # break out of for loop
                else: # if zipcode does not exist
                    exists = False # mark it not existing

            if(exists == False): # if zipcode not found in zipcodes list
                new_zipcode = Zipcode(entry) # create new zipcode object
                zipcodes.append(new_zipcode) # append it to list of zipcodes
