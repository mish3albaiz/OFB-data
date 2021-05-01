# main.py - Python script to fetch, process, and chart data in specified by ZIP Code.
# 4/28/2021
#
# Meshal Albaiz

from indices import * # imports question indices
from chart_data import * # imports functions to chart
from process_data import * # imports module that processes data
from get_data import * # import module that fetches data

download_csv() # download csv file of most recent update to entry database
open_csv() # open csv file and populate lists, create zipcode objects
process_entries() # process entries and calculate answers
plot_bars("hunger", hunger_i, yes_color="r") # plot questions with corresponding data in bar pairs
plot_bars("near_hunger", near_hunger_i, yes_color="r")
plot_bars("knows_pantry", knows_pantry_i, yes_color="b")
plot_bars("visited_pantry", visited_pantry_i, yes_color="b")
plot_bars("smartphone", smartphone_i, yes_color="b")
plot_bars("internet", internet_i, yes_color="b")
plot_bars("car", car_i, yes_color="b")
plot_bars("bicycle", bicycle_i, yes_color="b")
plot_bars("employed", employed_i, yes_color="b")
plot_bars("homeless", homeless_i, yes_color="r")
plot_bars("hardship", hardship_i, yes_color="r")
plot_bars("reach", reach_i, yes_color="r")
plot_bars("causes", causes_i, yes_color="r")
plot_pie_zipcode("ZIP Codes") # pie chart of zip code representation
plot_pie_volunteer("Volunteers vs. Non-Volunteers") # pie chart of volunteer percentage
