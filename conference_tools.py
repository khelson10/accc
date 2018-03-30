# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:33:08 2018

@author: khelson
"""
import numpy as np
import csv
import pickle as pickle
import datetime

class conference(object):
    
    def __init__(self, name = 'ACCC'):
        
        self.name = name
        self.teams = []
        self.riders = []
        self.bib_index = []
        self.team_index = []
        self.ind_omnium = []
        self.team_omnium = []
        self.races = []
        
    def build_riders(self, bib_filename = './accc_bibs.csv'):
        
        with open(bib_filename, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            bib_database = list(reader)
        for entry in bib_database[1:]:
            bib = entry[0]
            if bib < 100 or (bib < 300 and bib > 199) or (bib < 500 and bib > 399) or bib > 600:
                gender = 'M'
            else:
                gender = 'F'
            if entry[1] != '':

                new_rider = rider(bib, entry[1], entry[2], entry[3], 'school', gender, entry[7])
                self.bib_index.append(int(bib))
                self.riders.append(new_rider)

    def roster(self):
        for athlete in self.riders:
            print athlete.last_name, athlete.first_name, athlete.bib, athlete.licenseNprint 

    def add_rider(self, bib, licence, last, first, school, gender, cat, points = 0):
        
        new_rider = rider(int(bib), licence, last, first, school, gender, cat)
        
        self.riders.append(new_rider)
        self.bib_index.append(int(bib))
        try:
            self.teams[self.team_index.index(school)].add_rider(new_rider)
        except ValueError:
             print("school not found:")
             print school
             print "Adding school"
             
             self.add_team(school, [new_rider])

    def add_team(self, team_name, riders = []):
        
        new_team = team(team_name)
        self.team_index.append(team_name)
        self.teams.append(new_team)
        
        for racer in riders:
            
            new_team.add_rider(racer)
        
    def build_teams(self):

        for person in self.riders:
            
            self.team_index.append(person.team)
            
        self.team_index = list(set(self.team_index))
        
        for club in self.team_index:
            
            new_team = team(club)
        
            for athlete in self.riders:
                if athlete.team == club:
                    new_team.members.append(athlete)

            self.teams.append(new_team)
            
    def score_race(self, race_name, race_filename = './unc_rr_results.csv',
                   points_schedule = './points_schedule.csv'):
            
        new_race = race(name = race_name)
        
        with open(race_filename, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            race_results = list(reader)

        new_race.score_race(race_results, points_schedule)
        points = new_race.results        
        self.races.append(new_race)
        
        for entry in points:
            #print entry
            bib = entry[0]
            try:
                self.riders[self.bib_index.index(bib)].update_points(entry[1])
            except ValueError:
                print("RIDER NOT FOUND:")
                print bib
                print "Adding Nameless Rider"
                self.add_rider(bib, 0000000, 
                               'FIND last Name', 'FIND first name', 
                               'Find school', 'find gender', entry[2], points = entry[1])
            
    def compute_ind_omnium(self):    
        
        #loop over riders and compute scores for each category
        return None
        
    
    def save_conference(self):
        
        format = '%Y%m%d%H%M%S'
        
        path = './' + self.name + datetime.datetime.now().strftime(format) +'.pk'
        with open(path, 'wb') as output:
            pickle.dump(self.__dict__, output, pickle.HIGHEST_PROTOCOL)
        
class race(object):
    
    def __init__(self, name = None):
        
        self.name = name        
        self.results = None
        
    def score_race(self, race_results, points_schedule = './points_schedule.csv'):
        points_schedule = './points_schedule.csv'

        with open(points_schedule, 'rb') as csvfile:
            reader = csv.reader(csvfile)
            points_schedule = list(reader)
        points_list = []
        
        for entry in race_results[1:]:

            race_type = entry[0]
            if race_type != '':
                place = int(entry[2])
                bib = int(entry[3])

                points_type = entry[1]+race_type
                points_index = int(points_schedule[0].index(points_type))

                if place > 20:
                    points = 0
                else:
                    points = int(points_schedule[place][points_index])

                rider_result = [bib, points, entry[1]]
            points_list.append(rider_result)
        
        #loop over race results and compute points
        self.results = points_list
        
class team(object):
    
    def __init__(self, name):
        
        self.name = name
        self.members = []
        self.team_omnium_scorers = []
        self.MA = []
        self.MB = []
        self.MC = []
        self.MD = []
        self.WA = []
        self.WB = []
        self.WC = []
        self.WD = []
        

    def add_rider(self, rider):
        
        self.members.append(rider)
        
        if rider.gender == 'M':
            if rider.category == 'A':
                self.MA.append(rider)
            if rider.category == 'B':
                self.MB.append(rider)
            if rider.category == 'C':
                self.MC.append(rider)
            if rider.category == 'D':
                self.MD.append(rider)
        else:
            if rider.category == 'A':
                self.WA.append(rider)
            if rider.category == 'B':
                self.WB.append(rider)
            if rider.category == 'C':
                self.WC.append(rider)
            if rider.category == 'D':
                self.WD.append(rider)

    def calculate_omnium(self):
        
        scoring_riders = []
        self.team_omnium_scorers.append(scoring_riders)
                    
        
    def roster(self):
        
        for athlete in self.members:
            print athlete.last_name, athlete.first_name, athlete.bib, athlete.licenseN
        
class rider(object):
    
    def __init__(self, bib, licenseN, last, first, school, gender, category, points = 0):
        
        self.bib = int(bib)
        self.licenseN = int(licenseN)
        self.last_name = last
        self.team = school
        self.first_name = first
        self.gender = gender
        self.category = category
        self.category_old = None
        self.N_upgrades = 0
        self.points = points
        self.points_old = 0
        
    def update_points(self, points):
        self.points += points
        
    def category_upgrade(self, new_category, new_points = 0):
        
        if self.N_upgrades == 0:
            
            self.N_upgrades +=1
    
            self.category_old = self.category   
            self.points_old = self.points
        
            self.category = new_category
            self.points = new_points
        else:
            self.N_upgrades +=1
            
            self.category_old_old = self.category_old 
            self.points_old_old = self.points_old
    
            self.category_old = self.category   
            self.points_old = self.points
        
            self.category = new_category
            self.points = new_points
    
