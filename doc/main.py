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
import jieba
import copy
import sys
sys.path.append("..")
from lib.functions import project4 as p4 

#==============================================================================
lexicon1 = set(pd.read_csv("../output/ground truth dictionary by group/group1.csv").dictionary)
lexicon2 = set(pd.read_csv("../output/ground truth dictionary by group/group2.csv").dictionary)
lexicon3 = set(pd.read_csv("../output/ground truth dictionary by group/group3.csv").dictionary)
lexicon4 = set(pd.read_csv("../output/ground truth dictionary by group/group4.csv").dictionary)
lexicon5 = set(pd.read_csv("../output/ground truth dictionary by group/group5.csv").dictionary)
#==============================================================================
dictionary = pd.read_csv("../output/onegram.csv")
Dictionary = dictionary.set_index('word').T.to_dict("index")['freq']
#==============================================================================
five_gram_dictionary = pd.read_csv("../output/5-gram.csv")
Five_gram_dictionary = five_gram_dictionary.set_index('5_gram').T.to_dict("index")['freq']
#==============================================================================
five_gram_dictionary_c = pd.read_csv("../output/relaxed1.df.csv")
Five_gram_dictionary_x = five_gram_dictionary_c.set_index('5_gram').T.to_dict("index")['freq']
five_gram_dictionary_c = pd.read_csv("../output/relaxed2.df.csv")
Five_gram_dictionary_x.update(five_gram_dictionary_c.set_index('5_gram').T.to_dict("index")['freq'])
five_gram_dictionary_c = pd.read_csv("../output/relaxed3.df.csv")
Five_gram_dictionary_x.update(five_gram_dictionary_c.set_index('5_gram').T.to_dict("index")['freq'])
five_gram_dictionary_c = pd.read_csv("../output/relaxed4.df.csv")
Five_gram_dictionary_x.update(five_gram_dictionary_c.set_index('5_gram').T.to_dict("index")['freq'])
five_gram_dictionary_c = pd.read_csv("../output/relaxed5.df.csv")
Five_gram_dictionary_x.update(five_gram_dictionary_c.set_index('5_gram').T.to_dict("index")['freq'])
#==============================================================================
error_detection = pd.read_csv("../output/orc5.csv")
Error_Detection = error_detection.loc[error_detection.correct_word==False]

Threshold = 10
for We in Error_Detection.word:

    
    Candidates = p4.candidate_search(Dictionary, We, Threshold)
    dist_score = p4.distance_score(Candidates, We, Threshold)
    a1=0.25
    a2=0.25
    a3=0.25
    a4=0.25
    simi_score = p4.similarity_score(Candidates, We, a1, a2, a3, a4)
    
    pop_score = p4.popularity_score(Candidates)
    
    
    
    exis_score = p4.existance_score(Candidates, lexicon)
    
    
    
    five_gram_e = Error_Detection.loc[Error_Detection.word==We]
    five_gram_list = []
    for i in range(4):
        five_gram_list.append(five_gram_e.iloc[0,3+i])
    five_gram_list.append(We)
    for i in range(4):
        five_gram_list.append(five_gram_e.iloc[0,7+i])
    Five_Gram_E = []
    for i in range(5):
        five_gram_string = ' '.join(five_gram_list[i:i+5])
        Five_Gram_E.append(five_gram_string)
                  
    
    exat_pop_score = p4.exact_popularity_score(Candidates, We, Five_Gram_E, Five_gram_dictionary)
    
    
    relax_pop_score = p4.relaxed_popularity_score(Candidates, We, Five_Gram_E, Five_gram_dictionary_x)

#------------------------------

import numpy as np
import os
from collections import Counter
import re, string
from string import digits

#file_object = open('../data/ground_truth/group1_00000005.txt')

TEXT = str()
dirpath = '../data/ground_truth/'
for root, dirs, files in os.walk(dirpath):
    for file in files:
        file_object = open(dirpath+file)
        try:
            file_context = file_object.read()
        finally:
            file_object.close()
        text = file_context.lower()
        exclude = set(string.punctuation)
        text = ''.join(ch for ch in text if ch not in exclude)
        remove_digits = str.maketrans('', '', digits)
        text = text.translate(remove_digits)

        TEXT = TEXT + text


data_ = jieba.cut(TEXT)
data = dict(Counter(data_))

data['rch']
# =============================================================================
# We = "eve"
# Wc = "King"
# test = ["apple bee car dog eve", "bee car dog eve fat", "car dog eve fat get", "dog eve fat get hi", "eve fat get hi ill"]
# grams_e = []
# grams_C_X = []
# for grams in test:
#     grams_e.append(grams.replace(We, Wc, 1))
# for i in range(5):
#     five_gram_s = list(jieba.cut(grams_e[i]))
#     for k in range(5):
#         if -i+4==k:
#             continue
#         else:
#             five_gram_s_copy = copy.deepcopy(five_gram_s)
#             five_gram_s_copy[2*k] = "*"
#             gram_c_x = "".join(five_gram_s_copy)
#             grams_C_X.append(gram_c_x)
#             
# print(grams_C_X)
# =============================================================================
# Feature
Feature = pd.DataFrame()
Feature["We"] = ["rah"]*10 + ["abc"]*10
Feature["Y"] = [0]*6+[1]+[0]*8+[1]+[0]*4
We_df = pd.DataFrame()
length = len(Candidates)
We_df["We"] = [We]*10

We_df["dist_score"] = 
# resample to balance label 1 and label 0
label_1 = Feature.loc[Feature.Y == 1]
for i in range(2):
    label_1 = label_1.append(label_1)
Feature = Freature.append(label_1)


CS.find_common_subsequences("qweert", "qwwert")