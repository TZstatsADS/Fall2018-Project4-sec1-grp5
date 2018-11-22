# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 15:18:26 2018

@author: Chenghao
"""
from pyxdameraulevenshtein import damerau_levenshtein_distance
from nltk.metrics.distance import edit_distance
import py_common_subseq.py_common_subseq as CS #Need to change xrange() as range()
import math
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
    def similarity_score(candidates, We, a1=0.25, a2=0.25, a3=0.25, a4=0.25):
        Score = {}
        for Wc in candidates:
            common_subsequences = CS.find_common_subsequences(Wc, We)
            lcs = sorted(common_subsequences, key=lambda x: len(x))[-1]
            
            
            IniLetter = We[0]
            EndLetter = We[-1]
            MidLetter = We[math.ceil(len(We)/2)]
            
            #LCS_1
            common_subseq_IntLetter = set([])
            for W in common_subsequences:
                if W.startswith(IniLetter):
                    common_subseq_IntLetter.add(W)
                 
            if len(common_subseq_IntLetter) == 0:
                lcs1 = ''
            else:
                lcs1 = sorted(common_subseq_IntLetter, key=lambda x: len(x))[-1]
            
            #LCS_z
            common_subseq_EndLetter = set([])
            for W in common_subsequences:
                if W.endswith(EndLetter):
                    common_subseq_EndLetter.add(W)
                    
            if len(common_subseq_EndLetter) == 0:
                lcsz = ''
            else:
                lcsz = sorted(common_subseq_EndLetter, key=lambda x: len(x))[-1]
            
            #LCS_n
            common_subseq_MidLetter = set([])
            for W in common_subsequences:
                if W.startswith(MidLetter):
                    common_subseq_MidLetter.add(W)
                    
            if len(common_subseq_MidLetter) == 0:
                lcsn = ''
            else:
                lcsn = sorted(common_subseq_MidLetter, key=lambda x: len(x))[-1]
                
            denom = len(Wc) + len(We)
            nlcs = (2*len(lcs)**2)/denom
            nmnlcs1 = (2*len(lcs1)**2)/denom
            nmnlcsn = (2*len(lcsn)**2)/denom
            nmnlcsz = (2*len(lcsz)**2)/denom
            score = a1*nlcs + a2*nmnlcs1 + a3*nmnlcsn + a4*nmnlcsz
            Score[Wc] = score
        
        return(Score)