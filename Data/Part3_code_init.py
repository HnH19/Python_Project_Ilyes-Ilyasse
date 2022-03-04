# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 2022

@author: Ilyès & Ilyasse
"""

import ast

with open('final_cluster_part3.txt') as f: # Default file operation mode is `r'
    items = f.read()
    f.close()

cluster = ast.literal_eval(items)

