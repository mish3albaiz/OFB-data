# zipcode_class.py - Python class of ZIP code, filters answers by zipcode
# 4/28/2021
#
# Meshal Albaiz

from indices import * # import question indices


class Zipcode:
    def __init__(self, entry): # for a new zipcode
        self.zipcode = entry[zipcode_index] # save zip code number
        self.zipcode_count = 1 # first zipcode of this number
        # set yes and no answer counts for every question
        self.oregon_res_y = 1 if entry[oregon_res_i] == "Yes" else 0
        self.oregon_res_n = 1 if entry[oregon_res_i] == "No" else 0

        self.volunteer_y = 1 if entry[volunteer_i] == "Yes" else 0
        self.volunteer_n = 1 if entry[volunteer_i] == "No" else 0

        self.hunger_y = 1 if entry[hunger_i] == "Yes" else 0
        self.hunger_n = 1 if entry[hunger_i] == "No" else 0

        self.near_hunger_y = 1 if entry[near_hunger_i] == "Yes" else 0
        self.near_hunger_n = 1 if entry[near_hunger_i] == "No" else 0

        self.knows_pantry_y = 1 if entry[knows_pantry_i] == "Yes" else 0
        self.knows_pantry_n = 1 if entry[knows_pantry_i] == "No" else 0

        self.visited_pantry_y = 1 if entry[visited_pantry_i] == "Yes" else 0
        self.visited_pantry_n = 1 if entry[visited_pantry_i] == "No" else 0

        self.smartphone_y = 1 if entry[smartphone_i] == "Yes" else 0
        self.smartphone_n = 1 if entry[smartphone_i] == "No" else 0

        self.internet_y = 1 if entry[internet_i] == "Yes" else 0
        self.internet_n = 1 if entry[internet_i] == "No" else 0

        self.car_y = 1 if entry[car_i] == "Yes" else 0
        self.car_n = 1 if entry[car_i] == "No" else 0

        self.bicycle_y = 1 if entry[bicycle_i] == "Yes" else 0
        self.bicycle_n = 1 if entry[bicycle_i] == "No" else 0

        self.employed_y = 1 if entry[employed_i] == "Yes" else 0
        self.employed_n = 1 if entry[employed_i] == "No" else 0

        self.homeless_y = 1 if entry[homeless_i] == "Yes" else 0
        self.homeless_n = 1 if entry[homeless_i] == "No" else 0

        self.hardship_y = 1 if entry[hardship_i] == "Yes" else 0
        self.hardship_n = 1 if entry[hardship_i] == "No" else 0

        self.reach_y = 1 if entry[reach_i] == "Yes" else 0
        self.reach_n = 1 if entry[reach_i] == "No" else 0

        self.causes_y = 1 if entry[causes_i] == "Yes" else 0
        self.causes_n = 1 if entry[causes_i] == "No" else 0

    def update_values(self, entry): # update existing zipcode
        self.zipcode_count = self.zipcode_count + 1 # increase count of this zipcode
        # update yes and no answer counts for every question
        self.oregon_res_y = self.oregon_res_y + 1 if entry[oregon_res_i] == "Yes" else self.oregon_res_y
        self.oregon_res_n = self.oregon_res_n + 1 if entry[oregon_res_i] == "No" else self.oregon_res_n

        self.volunteer_y = self.volunteer_y + 1 if entry[volunteer_i] == "Yes" else self.volunteer_y
        self.volunteer_n = self.volunteer_n + 1 if entry[volunteer_i] == "No" else self.volunteer_n

        self.hunger_y = self.hunger_y + 1 if entry[hunger_i] == "Yes" else self.hunger_y
        self.hunger_n = self.hunger_n + 1 if entry[hunger_i] == "No" else self.hunger_n

        self.near_hunger_y = self.near_hunger_y + 1 if entry[near_hunger_i] == "Yes" else self.near_hunger_y
        self.near_hunger_n = self.near_hunger_n + 1 if entry[near_hunger_i] == "No" else self.near_hunger_n

        self.knows_pantry_y = self.knows_pantry_y + 1 if entry[knows_pantry_i] == "Yes" else self.knows_pantry_y
        self.knows_pantry_n = self.knows_pantry_n + 1 if entry[knows_pantry_i] == "No" else self.knows_pantry_n

        self.visited_pantry_y = self.visited_pantry_y + 1 if entry[visited_pantry_i] == "Yes" else self.visited_pantry_y
        self.visited_pantry_n = self.visited_pantry_n + 1 if entry[visited_pantry_i] == "No" else self.visited_pantry_n

        self.smartphone_y = self.smartphone_y + 1 if entry[smartphone_i] == "Yes" else self.smartphone_y
        self.smartphone_n = self.smartphone_n + 1 if entry[smartphone_i] == "No" else self.smartphone_n

        self.internet_y = self.internet_y + 1 if entry[internet_i] == "Yes" else self.internet_y
        self.internet_n = self.internet_n + 1 if entry[internet_i] == "No" else self.internet_n

        self.car_y = self.car_y + 1 if entry[car_i] == "Yes" else self.car_y
        self.car_n = self.car_n + 1 if entry[car_i] == "No" else self.car_n

        self.bicycle_y = self.bicycle_y + 1 if entry[bicycle_i] == "Yes" else self.bicycle_y
        self.bicycle_n = self.bicycle_n + 1 if entry[bicycle_i] == "No" else self.bicycle_n

        self.employed_y = self.employed_y + 1 if entry[employed_i] == "Yes" else self.employed_y
        self.employed_n = self.employed_n + 1 if entry[employed_i] == "No" else self.employed_n

        self.homeless_y = self.homeless_y + 1 if entry[homeless_i] == "Yes" else self.homeless_y
        self.homeless_n = self.homeless_n + 1 if entry[homeless_i] == "No" else self.homeless_n

        self.hardship_y = self.hardship_y + 1 if entry[hardship_i] == "Yes" else self.hardship_y
        self.hardship_n = self.hardship_n + 1 if entry[hardship_i] == "No" else self.hardship_n

        self.reach_y = self.reach_y + 1 if entry[reach_i] == "Yes" else self.reach_y
        self.reach_n = self.reach_n + 1 if entry[reach_i] == "No" else self.reach_n

        self.causes_y = self.causes_y + 1 if entry[causes_i] == "Yes" else self.causes_y
        self.causes_n = self.causes_n + 1 if entry[causes_i] == "No" else self.causes_n
