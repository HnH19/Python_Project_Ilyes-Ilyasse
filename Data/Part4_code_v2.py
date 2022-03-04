# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:36:25 2022

@author: Ilyès
"""

import os
import random as rd
import pandas as pd
import datetime as dt
import sqlite3
from sqlite3 import Error

from Part3_code import prob_0 as prob_onetime
from Part3_code import prob_1 as prob_business
from Part3_code import prob_2 as prob_retirement
from Part3_code import prob_3 as prob_healthy
from Part4_Client_IDs_Management import Client_IDs_Management
from Part4_goToRestaurant import goToRestaurant

from Part4_databaseFeed import insertVaribleIntoTable


# Create a class Clients and an empty database with some features to interact with it.

day_delta = dt.timedelta(days=1)
start_date = dt.date.today()
end_date = start_date + 36500 * day_delta



cols = ['TIME', 'CUSTOMERID', 'CUSTOMERTYPE', 'COURSE1', 'COURSE2', 'COURSE3', 'DRINKS1', 'DRINKS2',
           'DRINKS3', 'TOTAL1', 'TOTAL2', 'TOTAL3']

# # Creation of a database called "database" with columns name and index for each client ordering

database = pd.DataFrame(columns = cols)


window = (end_date - start_date).days
meal_type = ["Lunch", "Diner"]
clients_categories = ["Onetime", "Business", "Retirement", "Healthy"]
clients_distrib = [prob_onetime, prob_business, prob_retirement, prob_healthy]

Business_IDs = []
Healthy_IDs = []
Retirement_IDs = []

# Iteration over the days in the window to feed the database with data
for i in range(window):
    
    random_ID = rd.randint(0, 99999)
    # Creation of a random ID for each customer coming to the restaurant
    customerid = "ID" + str(random_ID)
    
    # Create a weighted choice between clients type.
    customertype = rd.choices(population = clients_categories, weights = clients_distrib, k=1)
    customertype = customertype[0]
    # k = 1 means that the list returned should contain only one element

    # Create a random choice between Lunch and Diner.
    meal = rd.choices(population = meal_type, weights = [0.5, 0.5], k=1)
    meal = meal[0]
    
    
    # Add each client ID coming to the restaurant into the clients IDs lists in order to them them after if they come back, notice that we don't store clients segmented as OneTime clients
    if customertype == ['Business']:
        Business_IDs.append(str(customerid))

    if customertype == ['Healthy']:
        Healthy_IDs.append(str(customerid))

    if customertype == ["Retirement"]:
        Retirement_IDs.append(str(customerid))

    else:
        customerid = customerid

    # Run the function to manage the IDs of clients
    Client_IDs_Management(customertype, customerid, Business_IDs, Healthy_IDs, Retirement_IDs)

    # Run the function to attribute the meals and dishes to each client
    goToRestaurant(customertype, customerid, Business_IDs, Healthy_IDs, Retirement_IDs)
    
    # print(Client_IDs_Management.id)
    
    # Assign dishes prices for the starter
    if goToRestaurant.starter == ['Soup']:
        price_starter = 3
    elif goToRestaurant.starter == ['Tomato-Mozzarella']:
        price_starter = 15
    elif goToRestaurant.starter == ['Oysters']:
        price_starter = 20
    else:
        price_starter = 0


    # Assign drinks costs paid by the customer for each course as a random float number between 0 and 3
    FC_drinks_paid = rd.uniform(0, 3)
    SC_drinks_paid = rd.uniform(0, 3)
    TC_drinks_paid = rd.uniform(0, 3)
    
    switch = 0
    spaghetti_price_increase = 5
    
    # Assign dishes prices for the main
    if goToRestaurant.main == ['Salad']:
        price_main = 9
    elif goToRestaurant.main == ['Spaghetti']:
        if switch == 0:
            price_main = 20
        if switch == 1:
            price_main = 20 + spaghetti_price_increase
            
    elif goToRestaurant.main == ['Steak']:
        price_main = 25
    elif goToRestaurant.main == ['Lobster']:
        price_main = 40
    else:
        price_main = 0

    # Assign dishes prices for the desserts
    if goToRestaurant.dessert == ['Pie']:
        price_dessert = 10
    elif goToRestaurant.dessert == ['IceCream']:
        price_dessert = 15
    else:
        price_dessert = 0


    # Computation of the total price for each course for the client created
    
    FC_total_price = FC_drinks_paid + price_starter
    SC_total_price = FC_drinks_paid + price_main
    TC_total_price = FC_drinks_paid + price_dessert


    
    # x = insertVaribleIntoTable(Client_IDs_Management.id, meal, customertype, goToRestaurant.starter, goToRestaurant.main, goToRestaurant.dessert, FC_drinks_paid, SC_drinks_paid, TC_drinks_paid, FC_total_price, SC_total_price, TC_total_price)
    
    database.loc[i] = [meal, Client_IDs_Management.id, customertype, goToRestaurant.starter, goToRestaurant.main, goToRestaurant.dessert, FC_drinks_paid, SC_drinks_paid, TC_drinks_paid, FC_total_price, SC_total_price, TC_total_price]


#database export to CSV file

export_csv = database.to_csv(r'..\Results\export_part4_results.csv', index=None, header=True)
