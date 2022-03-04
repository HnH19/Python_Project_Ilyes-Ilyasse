# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 12:30:45 2022

@author: Ilyès
"""

from Part1_code import df
# from Part4_code_v2 import switch

# print(database)

"-------------------------HEALTHY DATA MANIPULATION------------------------------"

Healthy_number = database['CUSTOMERTYPE'].value_counts()

print(Healthy_number)

f = open('..\\Results\\results_comparison_with_data_provided.txt', 'w')

# print("-----------TOTAL 1 Analysis---------------")
# print("OUR DATA")
# print(database['TOTAL1'].describe())
# print("DATA PROVIDED")
# print(df['FIRST_COURSE'].describe())
f.write("-----------TOTAL 1 (First Course) Analysis---------------\n")
f.write("*********OUR DATA**************\n")
f.write(str(database['TOTAL1'].describe()) + "\n")
f.write("*********DATA PROVIDED*********\n")
f.write(str(df['FIRST_COURSE'].describe()) + "\n")



# print("-----------TOTAL 2 Analysis---------------")

# print("OUR DATA")
# print(database['TOTAL2'].describe())
# print("DATA PROVIDED")
# print(df['SECOND_COURSE'].describe())

f.write("-----------TOTAL 2 (Second Course) Analysis---------------\n")
f.write("*********OUR DATA**************\n")
f.write(str(database['TOTAL2'].describe()) + "\n")
f.write("*********DATA PROVIDED*********\n")
f.write(str(df['SECOND_COURSE'].describe()) + "\n")


# print("-----------TOTAL 3 Analysis---------------")

# print("OUR DATA")
# print(database['TOTAL3'].describe())
# print("DATA PROVIDED")
# print(df['THIRD_COURSE'].describe())

f.write("-----------TOTAL 3 (Third Course) Analysis---------------\n")
f.write("*********OUR DATA**************\n")
f.write(str(database['TOTAL3'].describe()) + "\n")
f.write("*********DATA PROVIDED*********\n")
f.write(str(df['THIRD_COURSE'].describe()) + "\n")

f.close()

total_score_Onetime = 0
FC_score_Onetime = 0

db_Healthy = database.loc[database['CUSTOMERTYPE'] == 'Healthy']

FC_score_H = 0
SC_score_H = 0
TC_score_H = 0

for target1 in db_Healthy['TOTAL1']:
    FC_score_H = FC_score_H + target1

for target2 in db_Healthy['TOTAL2']:
    SC_score_H = SC_score_H + target2

for target3 in db_Healthy['TOTAL3']:
    TC_score_H = TC_score_H + target3

print("The overall paid by Healthy Clients in First Course is :", FC_score_H)
print("The overall paid by Healthy Clients in Second Course is :", SC_score_H)
print("The overall paid by Healthy Clients in Third Course is :", TC_score_H)

Total_Revenue_H = FC_score_H + SC_score_H + TC_score_H
Twice_Total_Revenue_H = Total_Revenue_H * 2

FC_total_score = 0
SC_total_score = 0
TC_total_score = 0

for point1 in database['TOTAL1']:
    FC_total_score = FC_total_score + point1

for point2 in database['TOTAL2']:
    SC_total_score = SC_total_score + point2

for point3 in database['TOTAL3']:
    TC_total_score = TC_total_score + point3
    
Total_Revenue = FC_total_score + SC_total_score + TC_total_score

Switched_Total_Revenue = Total_Revenue - Total_Revenue_H + Twice_Total_Revenue_H

print("Total Revenue is :", Total_Revenue)
print("If suddenly the restaurant had twice more healthy customers, the total revenue would be", Switched_Total_Revenue)

"-------------------------SPAGHETTI DATA MANIPULATION------------------------------"
switch = 1

if switch == 0:
    print("The price of Spaghetti is unchanged, the total revenue of the restaurant is", Total_Revenue)
if switch == 1:
    print("The total Revenue when the Spaghetti price increase by ", switch*5, "is", Total_Revenue)

"-------------------------Other research question------------------------------"
"How would the revenue would be affected if business clients won't come anymore"

db_Healthy = database.loc[database['CUSTOMERTYPE'] == 'Business']

FC_score_B= 0
SC_score_B = 0
TC_score_B = 0

for target1 in db_Healthy['TOTAL1']:
    FC_score_B = FC_score_B + target1

for target2 in db_Healthy['TOTAL2']:
    SC_score_B = SC_score_B + target2

for target3 in db_Healthy['TOTAL3']:
    TC_score_B = TC_score_B + target3

Total_Revenue_B = FC_score_B + SC_score_B + TC_score_B

print("The total Revenue of the restaurant without any Business client would be :", Total_Revenue - Total_Revenue_B)