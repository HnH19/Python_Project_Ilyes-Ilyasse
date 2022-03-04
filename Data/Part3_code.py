# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 2022

@author: Ilyès & Ilyasse
"""

import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import ast
from Part3_code_init import cluster


# print("own labels :", cluster)

datapath = os.path.abspath("../Data/part3.csv")
data = pd.read_csv(datapath, sep=",")

df =  pd.DataFrame(data)

list = []

for label in cluster:
    list.append(label)

df_labels = pd.DataFrame(list, columns=['Clusters'])

frames = [df, df_labels]

df_final = pd.concat(frames, axis = 1)

"--------------- CHECKING -----------------"
score = 0

client_type = df_final["CLIENT_TYPE"].values
clusters = df_final["Clusters"].values

for element, target in zip(client_type, clusters):
    if element == 'Onetime' and target == 0 or element == 'Business' and target == 1 or element == 'Retirement' and target == 2 or element == 'Healthy' and target == 3:
        score = score + 1
    else:
        score = score

print("score :", score)

prediction_accuracy = (score / 36500) * 100

print("The accuracy of our prediction is", prediction_accuracy, "%")
print("---------------------")
print("Reminder of our own labels stored in the cluster variable:")
print("0 : Onetime")
print("1 : Business")
print("2 : Retirement")
print("3 : Sport")

"--------------- Distribution of Clients using our own labels -----------------"

onetime_score = 0
business_score = 0
retirement_score = 0
sport_score = 0

for point in clusters:
    if point == 0:
        onetime_score = onetime_score + 1
    if point == 1:
        business_score = business_score + 1
    if point == 2:
        retirement_score = retirement_score + 1
    if point == 3:
        sport_score = sport_score + 1

print("Onetime score :", onetime_score)
print("Business score :", business_score)
print("Retirement score :", retirement_score)
print("Healthy score :", sport_score)

prob_0 = onetime_score/36500
prob_1 = business_score/36500
prob_2 = retirement_score/36500
prob_3 = sport_score/36500

print("Probability that this client is a Onetime client is :", prob_0)
print("Probability that this client is a Business client is :", prob_1)
print("Probability that this client is a Retirement client is :", prob_2)
print("Probability that this client is a Healthy client is :", prob_3)


"---------------------------Likelihood of a certain client to order a certain course----------------------------------------"

Starters = ["Soup", "Tomato-Mozarella", "Oysters"]
Mains = ["Salad", "Spaghetti", "Steak", "Lobster"]
Desserts = ["Ice Cream", "Pie"]

from Part1_code import FC_dishes_selected
from Part1_code import SC_dishes_selected
from Part1_code import TC_dishes_selected

df_FC_dishes_selected = pd.DataFrame (FC_dishes_selected, columns = ['FC dish selected by client'])
df_SC_dishes_selected = pd.DataFrame (SC_dishes_selected, columns = ['SC dish selected by client'])
df_TC_dishes_selected = pd.DataFrame (TC_dishes_selected, columns = ['TC dish selected by client'])

list_ = list.copy()
list_cat = []

for label in list_:
    if label == 0:
        list_cat.append('Onetime')
    if label == 1:
        list_cat.append('Business')
    if label == 2:
        list_cat.append('Retirement')
    if label ==3:
        list_cat.append('Healthy')
        
        

df_labels = pd.DataFrame(list_cat, columns = ['labels'])

modules = [df_FC_dishes_selected, df_SC_dishes_selected, df_TC_dishes_selected, df_labels]

df_dishes_selected = pd.concat(modules, axis = 1)

Onetime_FC_score = 0
Onetime_SC_score = 0
Onetime_TC_score = 0

Business_FC_score = 0
Business_SC_score = 0
Business_TC_score = 0

Retirement_FC_score = 0
Retirement_SC_score = 0
Retirement_TC_score = 0

Healthy_FC_score = 0
Healthy_SC_score = 0
Healthy_TC_score = 0

FC_dish = df_dishes_selected["FC dish selected by client"].values
SC_dish = df_dishes_selected["SC dish selected by client"].values
TC_dish = df_dishes_selected["TC dish selected by client"].values
category = df_dishes_selected["labels"].values

for a,b,c,d in zip(FC_dish, SC_dish, TC_dish, category):
    if d == 'Onetime':
        if a != 'just drinks':
            Onetime_FC_score = Onetime_FC_score + 1
        if b != 'just drinks':
            Onetime_SC_score = Onetime_SC_score + 1
        if c != 'just drinks':
            Onetime_TC_score = Onetime_TC_score + 1

    if d == 'Business':
        if a != 'just drinks':
            Business_FC_score = Business_FC_score + 1
        if b != 'just drinks':
            Business_SC_score = Business_SC_score + 1
        if c != 'just drinks':
            Business_TC_score = Business_TC_score + 1

    if d == 'Retirement':
        if a != 'just drinks':
            Retirement_FC_score = Retirement_FC_score + 1
        if b != 'just drinks':
            Retirement_SC_score = Retirement_SC_score + 1
        if c != 'just drinks':
            Retirement_TC_score = Retirement_TC_score + 1

    if d == 'Healthy':
        if a != 'just drinks':
            Healthy_FC_score = Healthy_FC_score + 1
        if b != 'just drinks':
            Healthy_SC_score = Healthy_SC_score + 1
        if c != 'just drinks':
            Healthy_TC_score = Healthy_TC_score + 1


Proba_Onetime_FC = Onetime_FC_score / onetime_score
Proba_Onetime_SC = Onetime_SC_score / onetime_score
Proba_Onetime_TC = Onetime_TC_score / onetime_score

Proba_Business_FC = Business_FC_score / business_score
Proba_Business_SC = Business_SC_score / business_score
Proba_Business_TC = Business_TC_score / business_score

Proba_Retirement_FC = Retirement_FC_score / retirement_score
Proba_Retirement_SC = Retirement_SC_score / retirement_score
Proba_Retirement_TC = Retirement_TC_score / retirement_score

Proba_Healthy_FC = Healthy_FC_score / sport_score
Proba_Healthy_SC = Healthy_SC_score / sport_score
Proba_Healthy_TC = Healthy_TC_score / sport_score

print("Likelihood that a Onetime client will order First Course is :", Proba_Onetime_FC)
print("Likelihood that a Onetime client will order Second Course is :", Proba_Onetime_SC)
print("Likelihood that a Onetime client will order Third Course is :", Proba_Onetime_TC)

print("Likelihood that a Business client will order First Course is :", Proba_Business_FC)
print("Likelihood that a Business client will order Second Course is :", Proba_Business_SC)
print("Likelihood that a Business client will order Third Course is :", Proba_Business_TC)

print("Likelihood that a Retirement client will order First Course is :", Proba_Retirement_FC)
print("Likelihood that a Retirement client will order Second Course is :", Proba_Retirement_SC)
print("Likelihood that a Retirement client will order Third Course is :", Proba_Retirement_TC)

print("Likelihood that a Healthy client will order First Course is :", Proba_Healthy_FC)
print("Likelihood that a Healthy client will order Second Course is :", Proba_Healthy_SC)
print("Likelihood that a Healthy client will order Third Course is :", Proba_Healthy_TC)

matrix_proba_course = [[ Proba_Onetime_FC,  Proba_Onetime_SC,  Proba_Onetime_TC],
       [ Proba_Business_FC,  Proba_Business_SC,  Proba_Business_TC],
       [ Proba_Retirement_FC,  Proba_Retirement_SC,  Proba_Retirement_TC],
       [ Proba_Healthy_FC,  Proba_Healthy_SC,  Proba_Healthy_TC]]

"--------------------------Probability of Client ordering a dish-------------------------------------"

"-----------------------------One Time Type of Client-----------------------------------------------"

dishes_score_Onetime = [[ 0,  0,  0], [0,  0,  0, 0], [ 0,  0]]

Starters = ["Soup", "Tomato-Mozarella", "Oysters"]
Mains = ["Salad", "Spaghetti", "Steak", "Lobster"]
Desserts = ["Ice Cream", "Pie"]


for e,f,g,h in zip(FC_dish, SC_dish, TC_dish, category):
    if h == 'Onetime':
        if e == 'just drinks':
            pass
        if e == 'Soup':
            dishes_score_Onetime[0][0] = dishes_score_Onetime[0][0] + 1
        if e == 'Tomato-Mozarella':
            dishes_score_Onetime[0][1] = dishes_score_Onetime[0][1] + 1
        if e == 'Oysters':
            dishes_score_Onetime[0][2] = dishes_score_Onetime[0][2] + 1

        if f == 'just drinks':
            pass
        if f == 'Salad':
            dishes_score_Onetime[0][1] = dishes_score_Onetime[0][1] + 1
        if f == 'Spaghetti':
            dishes_score_Onetime[1][1] = dishes_score_Onetime[1][1] + 1
        if f == 'Steak':
            dishes_score_Onetime[1][2] = dishes_score_Onetime[1][2] + 1
        if f == 'Lobster':
            dishes_score_Onetime[1][3] = dishes_score_Onetime[1][3] + 1
    
        if g == 'just drinks':
            pass
        if g == 'Ice Cream':
            dishes_score_Onetime[2][0] = dishes_score_Onetime[2][0] + 1
        if g == 'Pie':
            dishes_score_Onetime[2][1] = dishes_score_Onetime[2][1] + 1

copy = dishes_score_Onetime

summ1 = sum(copy[0])
summ2 = sum(copy[1])
summ3 = sum(copy[2])
           
proba_Onetime_Soup = dishes_score_Onetime[0][0] / summ1
proba_Onetime_Tomato_Mozarella = dishes_score_Onetime[0][1] / summ1
proba_Onetime_Oysters = dishes_score_Onetime[0][2] / summ1

proba_Onetime_Salad = dishes_score_Onetime[1][0] / summ2
proba_Onetime_Spaghetti = dishes_score_Onetime[1][1] / summ2
proba_Onetime_Steak = dishes_score_Onetime[1][2] / summ2
proba_Onetime_Lobster = dishes_score_Onetime[1][3] / summ2

proba_Onetime_IceCream = dishes_score_Onetime[2][0] / summ3
proba_Onetime_Pie = dishes_score_Onetime[2][1] / summ3

OFC = [ proba_Onetime_Soup,  proba_Onetime_Tomato_Mozarella,  proba_Onetime_Oysters]
OSC= [proba_Onetime_Salad,  proba_Onetime_Spaghetti,  proba_Onetime_Steak, proba_Onetime_Lobster]
OTC = [ proba_Onetime_IceCream,  proba_Onetime_Pie]

proba_dishes_Onetime = [OFC, OSC, OTC]

plt.bar(Starters, OFC, width = 0.5, color = 'red')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))


plt.bar(Mains, OSC, width = 0.5, color = 'yellow')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))


plt.bar(Desserts, OTC, width = 0.5, color = 'blue')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))
plt.title("Distribution of Dishes - 1st, 2nd & 3rd Courses - One Time Client Category")
plt.savefig("../Results/distrib_dishes_onetimeclient.pdf")
plt.clf()


"-----------------------------Business Type of Client-----------------------------------------------"

dishes_score_Business = [[ 0,  0,  0], [0,  0,  0, 0], [ 0,  0]]

Starters = ["Soup", "Tomato-Mozarella", "Oysters"]
Mains = ["Salad", "Spaghetti", "Steak", "Lobster"]
Desserts = ["Ice Cream", "Pie"]


for e,f,g,h in zip(FC_dish, SC_dish, TC_dish, category):
    if h == 'Business':
        if e == 'just drinks':
            pass
        if e == 'Soup':
            dishes_score_Business[0][0] = dishes_score_Business[0][0] + 1
        if e == 'Tomato-Mozarella':
            dishes_score_Business[0][1] = dishes_score_Business[0][1] + 1
        if e == 'Oysters':
            dishes_score_Business[0][2] = dishes_score_Business[0][2] + 1

        if f == 'just drinks':
            pass
        if f == 'Salad':
            dishes_score_Business[0][1] = dishes_score_Business[0][1] + 1
        if f == 'Spaghetti':
            dishes_score_Business[1][1] = dishes_score_Business[1][1] + 1
        if f == 'Steak':
            dishes_score_Business[1][2] = dishes_score_Business[1][2] + 1
        if f == 'Lobster':
            dishes_score_Business[1][3] = dishes_score_Business[1][3] + 1
    
        if g == 'just drinks':
            pass
        if g == 'Ice Cream':
            dishes_score_Business[2][0] = dishes_score_Business[2][0] + 1
        if g == 'Pie':
            dishes_score_Business[2][1] = dishes_score_Business[2][1] + 1

copy = dishes_score_Business

summ1 = sum(copy[0])
summ2 = sum(copy[1])
summ3 = sum(copy[2])
           
proba_Business_Soup = dishes_score_Business[0][0] / summ1
proba_Business_Tomato_Mozarella = dishes_score_Business[0][1] / summ1
proba_Business_Oysters = dishes_score_Business[0][2] / summ1

proba_Business_Salad = dishes_score_Business[1][0] / summ2
proba_Business_Spaghetti = dishes_score_Business[1][1] / summ2
proba_Business_Steak = dishes_score_Business[1][2] / summ2
proba_Business_Lobster = dishes_score_Business[1][3] / summ2

proba_Business_IceCream = dishes_score_Business[2][0] / summ3
proba_Business_Pie = dishes_score_Business[2][1] / summ3


BFC = [ proba_Business_Soup,  proba_Business_Tomato_Mozarella,  proba_Business_Oysters]
BSC= [proba_Business_Salad,  proba_Business_Spaghetti,  proba_Business_Steak, proba_Business_Lobster]
BTC = [ proba_Business_IceCream,  proba_Business_Pie]

proba_dishes_Business = [BFC, BSC, BTC]

plt.bar(Starters, BFC, width = 0.5, color = 'red')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))


plt.bar(Mains, BSC, width = 0.5, color = 'yellow')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))


plt.bar(Desserts, BTC, width = 0.5, color = 'blue')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))
plt.title("Distribution of Dishes - 1st, 2nd & 3rd Courses - Business Client Category")
plt.savefig("../Results/distrib_dishes_businessclient.pdf")
plt.clf()

"-----------------------------Retirement Type of Client-----------------------------------------------"

dishes_score_Retirement = [[ 0,  0,  0], [0,  0,  0, 0], [ 0,  0]]

Starters = ["Soup", "Tomato-Mozarella", "Oysters"]
Mains = ["Salad", "Spaghetti", "Steak", "Lobster"]
Desserts = ["Ice Cream", "Pie"]


for e,f,g,h in zip(FC_dish, SC_dish, TC_dish, category):
    if h == 'Retirement':
        if e == 'just drinks':
            pass
        if e == 'Soup':
            dishes_score_Retirement[0][0] = dishes_score_Retirement[0][0] + 1
        if e == 'Tomato-Mozarella':
            dishes_score_Retirement[0][1] = dishes_score_Retirement[0][1] + 1
        if e == 'Oysters':
            dishes_score_Retirement[0][2] = dishes_score_Retirement[0][2] + 1

        if f == 'just drinks':
            pass
        if f == 'Salad':
            dishes_score_Retirement[0][1] = dishes_score_Retirement[0][1] + 1
        if f == 'Spaghetti':
            dishes_score_Retirement[1][1] = dishes_score_Retirement[1][1] + 1
        if f == 'Steak':
            dishes_score_Retirement[1][2] = dishes_score_Retirement[1][2] + 1
        if f == 'Lobster':
            dishes_score_Retirement[1][3] = dishes_score_Retirement[1][3] + 1
    
        if g == 'just drinks':
            pass
        if g == 'Ice Cream':
            dishes_score_Retirement[2][0] = dishes_score_Retirement[2][0] + 1
        if g == 'Pie':
            dishes_score_Retirement[2][1] = dishes_score_Retirement[2][1] + 1

copy = dishes_score_Retirement

summ1 = sum(copy[0])
summ2 = sum(copy[1])
summ3 = sum(copy[2])
           
proba_Retirement_Soup = dishes_score_Retirement[0][0] / summ1
proba_Retirement_Tomato_Mozarella = dishes_score_Retirement[0][1] / summ1
proba_Retirement_Oysters = dishes_score_Retirement[0][2] / summ1

proba_Retirement_Salad = dishes_score_Retirement[1][0] / summ2
proba_Retirement_Spaghetti = dishes_score_Retirement[1][1] / summ2
proba_Retirement_Steak = dishes_score_Retirement[1][2] / summ2
proba_Retirement_Lobster = dishes_score_Retirement[1][3] / summ2

proba_Retirement_IceCream = dishes_score_Retirement[2][0] / summ3
proba_Retirement_Pie = dishes_score_Retirement[2][1] / summ3


RFC = [ proba_Retirement_Soup,  proba_Retirement_Tomato_Mozarella,  proba_Retirement_Oysters]
RSC= [proba_Retirement_Salad,  proba_Retirement_Spaghetti,  proba_Retirement_Steak, proba_Retirement_Lobster]
RTC = [ proba_Retirement_IceCream,  proba_Retirement_Pie]

proba_dishes_Retirement = [RFC, RSC, RTC]

plt.bar(Starters, RFC, width = 0.5, color = 'red')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))


plt.bar(Mains, RSC, width = 0.5, color = 'yellow')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))


plt.bar(Desserts, RTC, width = 0.5, color = 'blue')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))
plt.title("Distribution of Dishes - 1st, 2nd & 3rd Courses - Retirement Client Category")
plt.savefig("../Results/distrib_dishes_retirementclient.pdf")
plt.clf()

"-----------------------------Healthy Type of Client-----------------------------------------------"

dishes_score_Healthy = [[ 0,  0,  0], [0,  0,  0, 0], [ 0,  0]]

Starters = ["Soup", "Tomato-Mozarella", "Oysters"]
Mains = ["Salad", "Spaghetti", "Steak", "Lobster"]
Desserts = ["Ice Cream", "Pie"]


for e,f,g,h in zip(FC_dish, SC_dish, TC_dish, category):
    if h == 'Healthy':
        if e == 'just drinks':
            pass
        if e == 'Soup':
            dishes_score_Healthy[0][0] = dishes_score_Healthy[0][0] + 1
        if e == 'Tomato-Mozarella':
            dishes_score_Healthy[0][1] = dishes_score_Healthy[0][1] + 1
        if e == 'Oysters':
            dishes_score_Healthy[0][2] = dishes_score_Healthy[0][2] + 1

        if f == 'just drinks':
            pass
        if f == 'Salad':
            dishes_score_Healthy[0][1] = dishes_score_Healthy[0][1] + 1
        if f == 'Spaghetti':
            dishes_score_Healthy[1][1] = dishes_score_Healthy[1][1] + 1
        if f == 'Steak':
            dishes_score_Healthy[1][2] = dishes_score_Healthy[1][2] + 1
        if f == 'Lobster':
            dishes_score_Healthy[1][3] = dishes_score_Healthy[1][3] + 1
    
        if g == 'just drinks':
            pass
        if g == 'Ice Cream':
            dishes_score_Healthy[2][0] = dishes_score_Healthy[2][0] + 1
        if g == 'Pie':
            dishes_score_Healthy[2][1] = dishes_score_Healthy[2][1] + 1

copy = dishes_score_Healthy

summ1 = sum(copy[0])
summ2 = sum(copy[1])
summ3 = sum(copy[2])


proba_Healthy_Soup = dishes_score_Healthy[0][0] / summ1
proba_Healthy_Tomato_Mozarella = dishes_score_Healthy[0][1] / summ1
proba_Healthy_Oysters = dishes_score_Healthy[0][2] / summ1

proba_Healthy_Salad = dishes_score_Healthy[1][0] / summ2
proba_Healthy_Spaghetti = dishes_score_Healthy[1][1] / summ2
proba_Healthy_Steak = dishes_score_Healthy[1][2] / summ2
proba_Healthy_Lobster = dishes_score_Healthy[1][3] / summ2

proba_Healthy_IceCream = dishes_score_Healthy[2][0] / summ3
proba_Healthy_Pie = dishes_score_Healthy[2][1] / summ3

HFC = [ proba_Healthy_Soup,  proba_Healthy_Tomato_Mozarella,  proba_Healthy_Oysters]
HSC= [proba_Healthy_Salad,  proba_Healthy_Spaghetti,  proba_Healthy_Steak, proba_Healthy_Lobster]
HTC = [ proba_Healthy_IceCream,  proba_Healthy_Pie]

proba_dishes_Healthy = [HFC, HSC, HTC]

plt.bar(Starters, HFC, width = 0.5, color = 'red')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))


plt.bar(Mains, HSC, width = 0.5, color = 'yellow')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))


plt.bar(Desserts, HTC, width = 0.5, color = 'blue')
plt.ylabel("Probability", fontsize = 10)
plt.ylim((0,1))
plt.title("Distribution of Dishes - 1st, 2nd & 3rd Courses - Healthy Client Category")
plt.savefig("../Results/distrib_dishes_healthyclient.pdf")
plt.clf()


"-------------------------------Drinks Costs Distribution------------------------------------"

from Part1_code import drinks_costs, titles_list

plt.bar(titles_list, drinks_costs)
plt.ylabel("drinks costs only", fontsize = 10)
plt.title("Distribution of drinks costs only")
plt.savefig("../Results/distrib_drinks_costs.pdf")
