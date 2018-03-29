# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:33:08 2018

@author: khelson
"""

class conference(object):
    
    def __init__(self):
        
        self.teams = None
        self.riders = []
        self.ind_omnium = []
        self.team_omnium = []
        self.races = []
        
        
    def build_teams(self, bib_database):
        
        #open CSV
        #make list of teams
        teams = []
            
        self.teams.update(teams)
        
        
    def score_race(self, race_name, race_results):
            
        new_race = race(name = race_name)
        points = new_race.score_race(race_results)
        
        #loop over each         
        
        self.races.append(new_race)
        
    def compute_ind_omnium(self):    
        
        #loop over riders and compute scores for each category
        return None
        
        

class race(object):
    
    def __init__(self, name = None):
        
        self.name = name        
        self.results = None
        
    def score_race(self, race_results):
        points_list = []
        #loop over race results and compute points
        return points_list
        
        
class team(object):
    
    def __init__(self):
        
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
    
    def __init__(self, bib, licenseN, last, first, gender, category):
        
        self.bib = bib
        self.licenseN = licenseN
        self.last_name = last
        self.first_name = first
        self.gender = gender
        self.category = category
        self.category_old = None
        self.N_upgrades = 0
        self.points = 0
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
    