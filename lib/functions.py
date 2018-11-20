# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:18:26 2018

@author: Chenghao
"""
from pyxdameraulevenshtein import damerau_levenshtein_distance
import pandas as pd

# Candidate search
class project4():
    
    def candidate_search(Dictionary, We, threshold):
        candidate = {}
        for Wc in Dictionary:
            dist = damerau_levenshtein_distance(Wc, We)
            if dist <= threshold:
                candidate[Wc] = dist
                
        return(candidate)
        
#--------------------------------------
# Feature scoring
# Levenshtein edit distance
    def distance_score(candidates, We, threshold):
        Score = {}
        for Wc in candiates:
            score = 1 - 
            
        
        