# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:19:48 2018

@author: Chenghao
"""

from pyxdameraulevenshtein import damerau_levenshtein_distance
from nltk.metrics.distance import edit_distance
import pandas as pd
import sys
sys.path.append("..")
from lib.functions import project4 as p4 


Dictionary = pd.read_csv("../output/test_dictionary.csv").word
Threshold = 3
We = 'rah'
    
Candidate = p4.candidate_search(Dictionary, We, Threshold)
dist_score = p4.distance_score(Candidate, We, Threshold)

#------------------------------


