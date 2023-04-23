# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_vball_game.ipynb.

# %% auto 0
__all__ = ['VballGame']

# %% ../nbs/03_vball_game.ipynb 2
from nbdev.showdoc import *
from nbdev import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fastcore.basics import patch
from .vball_set import VballSet

# %% ../nbs/03_vball_game.ipynb 4
class VballGame:
    '''
    Creates a game with betwen 1 and 5 sets
    '''
    def __init__(self, 
             div:str): # The division of the set [PM, PW, RM, RW]
        # Set the point variables
        divisions = ["PM", "PW", "RM", "RW"]
        assert div in str(divisions), "Division is not valid must be: PM, PW, RM or RW"
        self.div = div
        self.n_sets = np.random.randint(3, 5 + 1)
        self.sets = []
        self.time = 0
        # TODO turn this into generator?
        for i in range(self.n_sets):
            self.sets.append(VballSet(self.div))
            self.time += self.sets[i].get_time()
            
               
        
    def __str__(self): return f"{self.div}{' game with '}{str(self.n_sets)}{' sets that takes '}{int(self.time/60)}{' minutes'}"
    def __repr__(self): return repr(f'VballSet("{self.div}")')

# %% ../nbs/03_vball_game.ipynb 6
@patch
def get_time(self:VballGame, # An function to output time of vball game
           ) -> float: # Returns the time of the set in seconds 
    return self.time
