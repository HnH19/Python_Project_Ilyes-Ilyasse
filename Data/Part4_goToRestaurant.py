# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 2022

@author: Ilyès
"""

import os
import random as rd

from Part3_code import Proba_Onetime_FC
from Part3_code import Proba_Onetime_SC
from Part3_code import Proba_Onetime_TC

from Part3_code import Proba_Business_FC
from Part3_code import Proba_Business_SC
from Part3_code import Proba_Business_TC

from Part3_code import Proba_Retirement_FC
from Part3_code import Proba_Retirement_SC
from Part3_code import Proba_Retirement_TC

from Part3_code import Proba_Healthy_FC
from Part3_code import Proba_Healthy_SC
from Part3_code import Proba_Healthy_TC

from Part3_code import proba_Onetime_Soup
from Part3_code import proba_Business_Soup
from Part3_code import proba_Retirement_Soup
from Part3_code import proba_Healthy_Soup

from Part3_code import proba_Onetime_Tomato_Mozarella
from Part3_code import proba_Business_Tomato_Mozarella
from Part3_code import proba_Retirement_Tomato_Mozarella
from Part3_code import proba_Healthy_Tomato_Mozarella

from Part3_code import proba_Onetime_Oysters
from Part3_code import proba_Business_Oysters
from Part3_code import proba_Retirement_Oysters
from Part3_code import proba_Healthy_Oysters

from Part3_code import proba_Onetime_Oysters
from Part3_code import proba_Business_Oysters
from Part3_code import proba_Retirement_Oysters
from Part3_code import proba_Healthy_Oysters

from Part3_code import proba_Onetime_Salad
from Part3_code import proba_Business_Salad
from Part3_code import proba_Retirement_Salad
from Part3_code import proba_Healthy_Salad

from Part3_code import proba_Onetime_Spaghetti
from Part3_code import proba_Business_Spaghetti
from Part3_code import proba_Retirement_Spaghetti
from Part3_code import proba_Healthy_Spaghetti

from Part3_code import proba_Onetime_Steak
from Part3_code import proba_Business_Steak
from Part3_code import proba_Retirement_Steak
from Part3_code import proba_Healthy_Steak

from Part3_code import proba_Onetime_Lobster
from Part3_code import proba_Business_Lobster
from Part3_code import proba_Retirement_Lobster
from Part3_code import proba_Healthy_Lobster

from Part3_code import proba_Onetime_IceCream
from Part3_code import proba_Business_IceCream
from Part3_code import proba_Retirement_IceCream
from Part3_code import proba_Healthy_IceCream

from Part3_code import proba_Onetime_Pie
from Part3_code import proba_Business_Pie
from Part3_code import proba_Retirement_Pie
from Part3_code import proba_Healthy_Pie

# Create a function which assign a starter, main dish and dessert to a client depending on his type.
def goToRestaurant(customertype, customerid, Business_IDs, Healthy_IDs, Retirement_IDs):

    if customertype == ['Business']:

        goToRestaurant.starter = rd.choices(
            population=["Nothing", "Oysters", "Tomato-Mozzarella", "Soup"],
            weights=[(1 - Proba_Business_FC), proba_Business_Oysters, proba_Business_Tomato_Mozarella, proba_Business_Soup],
            k=1
        )
        goToRestaurant.main = rd.choices(
            population=["Salad", "Spaghetti", "Steak", "Lobster"],
            weights=[proba_Business_Salad, proba_Business_Spaghetti, proba_Business_Steak, proba_Business_Lobster],
            k=1
        )
        goToRestaurant.dessert = rd.choices(
            population=["Nothing", "Pie", "IceCream"],
            weights=[(1 - Proba_Business_TC), proba_Business_Pie, proba_Business_IceCream],
            k=1
        )

    if customertype == ['Retirement']:
        goToRestaurant.starter = rd.choices(
            population=["Nothing", "Oysters", "Tomato-Mozzarella", "Soup"],
            weights=[(1 - Proba_Retirement_FC), proba_Retirement_Oysters, proba_Retirement_Tomato_Mozarella, proba_Retirement_Soup],
            k=1
        )
        goToRestaurant.main = rd.choices(
            population=["Salad", "Spaghetti", "Steak", "Lobster"],
            weights=[proba_Retirement_Salad, proba_Retirement_Spaghetti, proba_Retirement_Steak, proba_Retirement_Lobster],
            k=1
        )
        goToRestaurant.dessert = rd.choices(
            population=["Nothing", "Pie", "IceCream"],
            weights=[(1 - Proba_Retirement_TC), proba_Retirement_Pie, proba_Retirement_IceCream],
            k=1
        )


    if customertype == ['Healthy']:
        goToRestaurant.starter = rd.choices(
            population=["Nothing", "Oysters", "Tomato-Mozzarella", "Soup"],
            weights=[(1 - Proba_Healthy_FC), proba_Healthy_Oysters, proba_Healthy_Tomato_Mozarella, proba_Healthy_Soup],
            k=1
        )
        goToRestaurant.main = rd.choices(
            population=["Salad", "Spaghetti", "Steak", "Lobster"],
            weights=[proba_Healthy_Salad, proba_Healthy_Spaghetti, proba_Healthy_Steak, proba_Healthy_Lobster],
            k=1
        )
        goToRestaurant.dessert = rd.choices(
            population=["Nothing", "Pie", "IceCream"],
            weights=[(1 - Proba_Healthy_TC), proba_Healthy_Pie , proba_Healthy_IceCream],
            k=1
        )

    if customertype == ['Onetime']:
        goToRestaurant.starter = rd.choices(
            population=["Nothing", "Oysters", "Tomato-Mozzarella", "Soup"],
            weights=[(1 - Proba_Onetime_FC), proba_Onetime_Oysters, proba_Onetime_Tomato_Mozarella, proba_Onetime_Soup],
            k=1
        )
        goToRestaurant.main = rd.choices(
            population=["Salad", "Spaghetti", "Steak", "Lobster"],
            weights=[proba_Onetime_Salad, proba_Onetime_Spaghetti, proba_Onetime_Steak, proba_Onetime_Lobster],
            k=1
        )
        goToRestaurant.dessert = rd.choices(
            population=["Pie", "IceCream", "Nothing"],
            weights=[(1 - Proba_Onetime_TC), proba_Onetime_Pie, proba_Onetime_IceCream],
            k=1
        )