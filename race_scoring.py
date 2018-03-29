import numpy as np
import matplotlib.pyplot as plt
import csv

bib_filename = './accc_bibs.csv'

with open(bib_filename, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    bib_database = list(reader)

race_filename = './unc_rr_results.csv'

with open(race_filename, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    results_database = list(reader)

points_schedule = './points_schedule.csv'

with open(points_schedule, 'rb') as csvfile:
    reader = csv.reader(csvfile)
    points_schedule = list(reader)

rider_database = []

for entry in bib_database[1:]:
    bib = entry[0]
    if bib < 100 or (bib < 300 and bib > 199) or (bib < 500 and bib > 399) or bib > 600:
        gender = 'M'
    else:
        gender = 'F'
    if entry[1] != '':
        rider = [bib, entry[1], entry[2], entry[3], 'school', gender, entry[7], 0, 0, 0]
        rider_database.append(rider)

bib_index = [rider[0] for rider in rider_database]

race_results = []

for entry in results_database[1:]:

    race_type = entry[0]
    if race_type != '':
        place = int(entry[2])
        bib = entry[3]

        points_type = entry[1]+race_type
        points_index = int(points_schedule[0].index(points_type))

        if place > 20:
            points = 0
        else:
            points = int(points_schedule[place][points_index])

        rider_result = [bib, points]
        race_results.append(rider_result)

for result in race_results:
    bib = result[0]
    try:
        rider = bib_index.index(bib) 
        omnium_entry = rider_database[rider][:-1]
        omnium_entry.append(result[1])
        omnium_entry.append(np.sum(np.array(omnium_entry[7:])))
        ind_omnium.append(omnium_entry)
    except ValueError:
        print("RIDER NOT FOUND:")
        print bib
        print "\n"

       
    
    
