# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 21:41:50 2022

@author: Ilyès & Ilyasse

Part 1 Code - Project Python TSM

"""
import os
import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

f = open("../Data/part1.csv") #path pointing to the csv file

reader = csv.reader(f) #we create a reader to read the csv file using the csv package imported

list = []

for line in reader : #the reader created in an iterable object of lines from the CSV file, we can iterate over the lines of the CSV using a for loop
    
    list.append(line)

list.pop(0)

titles_list=['First_Course', 'Second_Course', 'Third_Course']

first_course_list=[]
second_course_list=[]
third_course_list=[]

for element in list:
    first_course_list.append(float(element[2]))
    second_course_list.append(float(element[3]))
    third_course_list.append(float(element[4]))

print("-------------COURSES COSTS ANALYSIS---------------------")

sum_first_course = 0
sum_second_course = 0
sum_third_course = 0

for cost1 in first_course_list:
    sum_first_course = sum_first_course + cost1

for cost2 in second_course_list:
    sum_second_course = sum_second_course + cost2

for cost3 in third_course_list:
    sum_third_course = sum_third_course + cost3

overall_costs = []

overall_costs.append(sum_first_course)
overall_costs.append(sum_second_course)
overall_costs.append(sum_third_course)

#print(sum_first_course)
#print(sum_second_course)
#print(sum_third_course)


fig = sns.histplot(data = first_course_list, bins = 50)
fig.set_xlabel("cost", fontsize = 10)
fig.set_ylabel("number ordered", fontsize = 10)
plt.title("Distribution of costs in First Course")
plt.savefig("../Results/distrib_course1.pdf")
print("The distribution of the cost in First Course is saved in distrib_course1.pdf on this folder")
plt.clf()

fig = sns.histplot(data = second_course_list, bins = 50)
fig.set_xlabel("cost", fontsize = 10)
fig.set_ylabel("number ordered", fontsize = 10)
plt.title("Distribution of costs in Second Course")
plt.savefig("../Results/distrib_course2.pdf")
print("The distribution of the cost in Second Course is saved in distrib_course2.pdf on this folder")
plt.clf()

fig = sns.histplot(data = third_course_list, bins = 100)
fig.set_xlabel("cost", fontsize = 10)
fig.set_ylabel("number ordered", fontsize = 10)
plt.title("Distribution of costs in Third Course")
plt.savefig("../Results/distrib_course3.pdf")
print("The distribution of the cost in Third Course is saved in distrib_course3.pdf on this folder")
plt.clf()

plt.bar(titles_list, overall_costs, color = 'green')
plt.ylabel("overall cost", fontsize = 10)
print("The distribution of the cost per course is saved in barplot_cost_percourse.pdf on this folder")
plt.savefig("../Results/barplot_cost_percourse.pdf")


print("-------------DRINKS COSTS ANALYSIS---------------------")

first_course_dishes = ['Soup', 'Tomato-Mozarella', 'Oysters']
second_course_dishes = ['Salad', 'Spaghetti', 'Steak', 'Lobster']
third_course_dishes = ['Ice Cream', 'Pie']
prices_first_course = [3, 15, 20]
prices_second_course = [9, 20, 25, 40]
prices_third_course = [15, 10]


diff=0
FC_drinks_cost_list = []
FC_dishes_selected = []
FC_prices_dishes_selected = []
FC_drink_selected_costs = []

'-------------------- FIRST COURSE ----------------------------'

for target in first_course_list:
    # print(target)
    diff_list=[]
    index=[]
    for i in range(3):
        if target > prices_first_course[i]:
            diff = target - prices_first_course[i]
            diff_list.append(diff)
            index.append(i)
        else:
            pass
        
    if target >= 3:
        # print(min(diff_list))
        a = diff_list.index(min(diff_list))
        dish_selected = first_course_dishes[index[a]]
        price_dish_selected = prices_first_course[index[a]]
        drink_cost = target - price_dish_selected
        
    if target <= 3:
        dish_selected = "just drinks"
        price_dish_selected = 0
        drink_cost=target
    # print(dish_selected)
    # print(price_dish_selected)
    #print(drink_cost)
    # print("finished")
    # print("-----------")
    
    FC_dishes_selected.append(dish_selected)
    FC_prices_dishes_selected.append(price_dish_selected)
    FC_drink_selected_costs.append(drink_cost)
    
    FC_drinks_cost_list.append(drink_cost)

FC_drinks = sum(FC_drinks_cost_list)
print("First Course Drinks Costs are", FC_drinks)

'-------------------- SECOND COURSE ----------------------------'

diff=0
SC_drinks_cost_list = []
SC_dishes_selected = []
SC_prices_dishes_selected = []
SC_drink_selected_costs = []


for main in second_course_list:
    #print(main)
    diff_list=[]
    index=[]
    for i in range(4):
        if main > prices_second_course[i]:
            diff = main - prices_second_course[i]
            diff_list.append(diff)
            index.append(i)
        else:
            pass
        
    if main >= 9:
        # print(min(diff_list))
        a = diff_list.index(min(diff_list))
        dish_selected = second_course_dishes[index[a]]
        price_dish_selected = prices_second_course[index[a]]
        drink_cost = main - price_dish_selected
        
    if main <= 9:
        dish_selected = "just drinks"
        price_dish_selected = 0
        drink_cost=main
    # print(dish_selected)
    # print(price_dish_selected)
    # print(drink_cost)
    # print("finished")
    # print("-----------")
    
    SC_dishes_selected.append(dish_selected)
    SC_prices_dishes_selected.append(price_dish_selected)
    SC_drink_selected_costs.append(drink_cost)
    
    SC_drinks_cost_list.append(drink_cost)
    

SC_drinks = sum(SC_drinks_cost_list)

print("Second Course Drinks Costs are", SC_drinks)

'-------------------- THIRD COURSE ----------------------------'

diff=0
TC_drinks_cost_list = []
TC_dishes_selected = []
TC_prices_dishes_selected = []
TC_drink_selected_costs = []


for dessert in third_course_list:
    # print(dessert)
    diff_list=[]
    index=[]
    for i in range(2):
        if dessert > prices_third_course[i]:
            diff = dessert - prices_third_course[i]
            diff_list.append(diff)
            index.append(i)
        else:
            pass
        
    if dessert >= 10:
        # print(min(diff_list))
        a = diff_list.index(min(diff_list))
        dish_selected = third_course_dishes[index[a]]
        price_dish_selected = prices_third_course[index[a]]
        drink_cost = dessert - price_dish_selected
        
    if dessert <= 10:
        dish_selected = "just drinks"
        price_dish_selected = 0
        drink_cost=dessert
    
    # print(dish_selected)
    # print(price_dish_selected)
    # print(drink_cost)
    # print("finished")
    # print("-----------")
    
    TC_dishes_selected.append(dish_selected)
    TC_prices_dishes_selected.append(price_dish_selected)
    TC_drink_selected_costs.append(drink_cost)
    
    TC_drinks_cost_list.append(drink_cost)
    

TC_drinks = sum(TC_drinks_cost_list)

print("Third Course Drinks Costs are", TC_drinks)

drinks_costs = [FC_drinks, SC_drinks, TC_drinks]

plt.bar(titles_list, drinks_costs, color = 'yellow')
plt.title("Distribution of costs per Course")
plt.ylabel("overall cost", fontsize = 10)

legend = plt.legend(["overall costs", "drinks costs"], title = "Legend")

plt.savefig("../Results/barplot_drinks_costs_percourse.pdf")



'-------------------------------'

datapath = os.path.abspath("../Data/part1.csv")
data = pd.read_csv(datapath, sep=",")

df =  pd.DataFrame(data)

df.insert(5, "Dishes selected First Course", FC_dishes_selected, True)
df.insert(6, "Price for Dish selected in First Course", FC_prices_dishes_selected, True)
df.insert(7, "Costs of drinks for Clients choosing First Course", FC_drinks_cost_list, True)

df.insert(8, "Dishes selected Second Course", SC_dishes_selected, True)
df.insert(9, "Price for Dish selected in Second Course", SC_prices_dishes_selected, True)
df.insert(10, "Costs of drinks for Clients choosing Second Course", SC_drinks_cost_list, True)

df.insert(11, "Dishes selected Third Course", TC_dishes_selected, True)
df.insert(12, "Price for Dish selected in Third Course", TC_prices_dishes_selected, True)
df.insert(13, "Costs of drinks for Clients choosing Third Course", TC_drinks_cost_list, True)



