# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_vball_set.ipynb.

# %% auto 0
__all__ = ['VballSet']

# %% ../nbs/02_vball_set.ipynb 2
from nbdev.showdoc import *
from nbdev import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fastcore.basics import patch

# %% ../nbs/02_vball_set.ipynb 10
class VballSet:
    '''
    Creates a set with and times the length of a set
    '''
    def __init__(self, 
                div:str, # The division of the set [PM, PW, RM, RW]
                set_5:bool = False): # Maximum number of points in a set
        # Set the point variables
        divisions = ["PM", "PW", "RM", "RW"]
        assert div in str(divisions), "Division is not valid must be: PM, PW, RM or RW"
        self.div = div
        if div == "PM" or div == "RM":
            self.point_mean = 4.99
            self.point_sd = 4.35
            self.rest_mean = 29.02
            self.rest_sd = 19.44
        else: 
            self.point_mean = 6.88
            self.point_sd = 5.92
            self.rest_mean = 28.92
            self.rest_sd = 18.21
            
        # set the max points and probability based on set number
        if set_5 == False:
            max_points = 25
            prob = 0.85
        else:
            max_points = 15
            prob = 0.7
        # Determine the number of points. 
        self.points = max_points + int(np.random.binomial(max_points - 2, prob, 1))
        # 1 lest rest than points as last point doesn't have a break
        self.rests = self.points - 1
        
        time_points = np.random.normal(self.point_mean, self.point_sd, self.points).sum()
        
        time_rests = np.random.normal(self.rest_mean, self.rest_sd, self.rests).sum()
        
        # 3 30s timeouts
        time_timeouts = 3 * 30
        
        self.time_set = time_points + time_rests + time_timeouts        
        
    def __str__(self): return f"{'Length of set is '}{int(self.time_set/60)}{' mins long'}"
    def __repr__(self): return repr(f'VballSet("{self.div}")')

# %% ../nbs/02_vball_set.ipynb 12
@patch
def get_time(self:VballSet, # An function to output time of set ofr vball set
           ) -> float: # Returns the time of the set in seconds 
    return self.time_set
