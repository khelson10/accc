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
            
        self.teams.append(teams)
        
        
    def score_race(self, race_name, race_results):
        
    
        
        
    def compute_ind_omnium(self):    
        
        #loop over riders and compute scores            

class race(object):
    
    def __init__(self):
        
        
        
        
class team(object):
    
    def __init__(self):
        
        self.members = []
        

    def add_rider(self, rider):
        
        self.members.append(rider)
        
    def roster(self):
        
        for athlete in self.members:
            print athlete.last_name, athlete.first_name, athlete.bib, athlete.licenseN
        
class rider(object):
    
    def __init__(self, bib, licenseN, last, first, category):
        
        self.bib = bib
        self.licenseN = licenseN
        self.last_name = last
        self.first_name = first
        self.category = category
        self.points = 0
        
    def update_points(self, points):
        self.points = points
    