# chart_data.py - Python script to chart data in specified manner
# 4/28/2021
#
# Meshal Albaiz

import matplotlib.pyplot as plt
# matplotlib is used for creating the charts
import numpy as np
from indices import * # question indices
from zipcode_class import Zipcode # import zipcode class
from process_data import * # import process data


# method to plot pairs of plot_bars
# inputs: value_string is the name of the string to be plotted
# question_index is the index of the question
# yes_color is the color of the "Yes" bar, this is used for emphasis on important data

def plot_bars(value_string, question_index, yes_color):
    string_y = value_string + "_y" # string of yes answers
    string_n = value_string + "_n" # string of no answers

    question = questions[question_index] # get question to use as title

    N = len(zipcodes) # number of bar pairs

    zipcode_list = [] # list of unique zipcodes
    answer_y = [] # list of yes answers corresponding to zipcodes
    answer_n = [] # list of no answers corresponding to zipcodes
    for item in zipcodes: # for each zipcode object
        zipcode_list.append(item.zipcode) # get zipcode
        answer_y.append(getattr(item, string_y)) # get yes answers
        answer_n.append(getattr(item, string_n)) # get no answers

    ind = np.arange(N) # set positions of zipcodes
    width = 0.35 # set width of bar

    if(yes_color == "b"): # set yes and no bars based on yes color input
        y_color = "cornflowerblue"
        n_color = "firebrick"
    else:
        y_color = "firebrick"
        n_color = "cornflowerblue"

    plt.bar(ind, answer_y, width, label='Yes', color=y_color) # plot yes bars
    plt.bar(ind + width, answer_n, width, label='No', color=n_color) # plot no bars

    plt.title(question, loc='center', wrap=True) # set title

    plt.xticks(ind + width / 2, zipcode_list, rotation='vertical') # configure x labels
    plt.legend(loc='best') # set legend
    plt.tight_layout(pad=4) # set padding around figure to fit long questions
    plt.savefig("./figures/" + value_string + '.png') # save figure as png
    plt.clf() # clear frame

def plot_pie_zipcode(title):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    zipcode_list = []
    count_list = []
    total_entries = 0
    for item in zipcodes:
        zipcode_list.append(item.zipcode)
        count_list.append(item.zipcode_count)
        total_entries = total_entries + item.zipcode_count
    labels = zipcode_list
    percentages = [count / total_entries for count in count_list]
    sizes = percentages

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title(title, y=1.05)
    plt.savefig("./figures/" + title + '.png')
    plt.clf()

def plot_pie_volunteer(title):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    non_count = 0
    volunteer_count = 0
    total_entries = 0
    for item in zipcodes:
        volunteer_count += item.volunteer_y
        non_count += item.volunteer_n
        total_entries = volunteer_count + non_count
        count_list = [volunteer_count, non_count]
    labels = ("Volunteers", "Non-Volunteers")
    percentages = [count / total_entries for count in count_list]
    sizes = percentages

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title(title, y=1.05)
    plt.savefig("./figures/" + title + '.png')
    plt.clf()
