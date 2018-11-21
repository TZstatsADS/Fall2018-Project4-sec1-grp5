# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:18:26 2018

@author: Chenghao
"""
from pyxdameraulevenshtein import damerau_levenshtein_distance
from nltk.metrics.distance import edit_distance
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
        for Wc in candidates:
            score = 1 - edit_distance(Wc, We, substitution_cost=1, transpositions=False)/(threshold + 1)
            Score[Wc] = score
            
        return(Score)
            
# String similarity
#    def similarity_score(candidates, We, a1, a2, a3, a4):
        
        