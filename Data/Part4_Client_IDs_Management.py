# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 08:10:29 2022

@author: Ilyès
"""

import os
import random as rd
import pandas as pd
import datetime as dt

# Function which manage the IDs of the clients according to their underlying distributions if they tend to come back to the restaurant or not
def Client_IDs_Management(customertype, customerid, Business_IDs, Healthy_IDs, Retirement_IDs):

    if customertype == ['Business']:

        Client_IDs_Management.id = rd.choices(
            population=[customerid, rd.choice(Business_IDs)],
            weights=[0.5, 0.5],
            k=1
        )
        Client_IDs_Management.id = Client_IDs_Management.id[0]

    elif customertype == ['Healthy']:
        Client_IDs_Management.id = rd.choices(
            population=[customerid, rd.choice(Healthy_IDs)],
            weights=[0.3, 0.7],
            k=1
        )
        Client_IDs_Management.id = Client_IDs_Management.id[0]

    elif customertype == ['Retirement']:
        Client_IDs_Management.id = rd.choices(
            population=[customerid, rd.choice(Retirement_IDs)],
            weights=[0.1, 0.9],
            k=1
        )
        Client_IDs_Management.id = Client_IDs_Management.id[0]

    else:
        Client_IDs_Management.id = customerid
