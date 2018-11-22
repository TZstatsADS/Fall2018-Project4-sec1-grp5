# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 14:19:48 2018

@author: Chenghao
"""

from pyxdameraulevenshtein import damerau_levenshtein_distance
from nltk.metrics.distance import edit_distance
import py_common_subseq.py_common_subseq as CS #Need to change xrange() as range()
import math
import pandas as pd
import sys
sys.path.append("..")
from lib.functions import project4 as p4 


Dictionary = pd.read_csv("../output/test_dictionary.csv").word
Threshold = 3
We = 'rah'
    
Candidates = p4.candidate_search(Dictionary, We, Threshold)
dist_score = p4.distance_score(Candidates, We, Threshold)

#------------------------------

a1=0.25
a2=0.25
a3=0.25
a4=0.25

simi_score = p4.similarity_score(Candidates, We, a1, a2, a3, a4)