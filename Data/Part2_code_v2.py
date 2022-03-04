# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 2022

@author: Ilyès & Ilyasse

Part 2 Code - Project Python TSM

"""

import os
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import numpy as np
from yellowbrick.cluster import KElbowVisualizer

datapath = os.path.abspath("../Data/part1.csv")
data = pd.read_csv(datapath, sep=",")

df =  pd.DataFrame(data)
clients = pd.DataFrame(df.iloc[:,0])

del df['TIME']
del df['CLIENT_ID']


"This part is used to compute the optimal number of clusters using an Elbow Curve---"
model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,12)).fit(df)
visualizer.show()
"---Uncomment this previous section to compute the optimal number of clusters-----"
"We will fix the number of clusters to 4 in the following"

X = df.values


def calculate_cost(X, centroids, cluster):
  sum = 0
  for i, val in enumerate(X):
    sum += np.sqrt((centroids[int(cluster[i]), 0]-val[0])**2 +(centroids[int(cluster[i]), 1]-val[1])**2)
  return sum

def kmeans(X, k):
  diff = 1
  cluster = np.zeros(X.shape[0])
  centroids = data.sample(n=k).values
  while diff:
      # for each observation
      for i, row in enumerate(X):
          mn_dist = float('inf')
         
          for idx, centroid in enumerate(centroids):
            d = np.sqrt((centroid[0]-row[0])**2 + (centroid[1]-row[1])**2)
            
            # store closest centroid
            if mn_dist > d:
                mn_dist = d
                cluster[i] = idx
      new_centroids = pd.DataFrame(X).groupby(by=cluster).mean().values
      # if centroids are same then leave
      if np.count_nonzero(centroids-new_centroids) == 0:
          diff = 0
      else:
        centroids = new_centroids
  return centroids, cluster

k = 4
centroids, cluster = kmeans(X, k)


# Create the figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Generate the values
x_vals = X[:, 0]
y_vals = X[:, 1]
z_vals = X[:, 2]

cluster = cluster.astype(int)



"-----UNCOMMENT THIS LINE TO WORK WITH THE CLUSTER ANALYSED------------"
from Part3_code_init import cluster
"-----------------------------------------------------------------------"
"The cluster computed by the user will be different from the one we stored"
"in the .txt file after we ran the code, on which we performed our analysis."
"Indeed, the machine learning process updates the labels at each run."

cols = [['red', 'green', 'blue', 'orange'][l] for l in cluster]

# Plot the values
ax.scatter(x_vals, y_vals, z_vals, c = cols, marker='x')
ax.set_xlabel('First Course Costs')
ax.set_ylabel('Second Course Costs')
ax.set_zlabel('Third Course Costs')

plt.title("Clusters Visualization in 3d - 1st, 2nd & 3rd Course")

plt.savefig("../Results/clusters_3d.pdf")


ax.cla()

print("------------------CLUSTERS VISUALIZATION------------------------------")
print("Please, see clusters vizualisation in 3D in this folder named clusters_3d.pdf")
print("Legend :")
print("Red : Label 0 : Onetime")
print("Green : Label 1 : Business")
print("Blue : Label 2 : Retirement")
print("Orange : Label 3 : Healthy")
print("The different clusters can also be observed in 2d in the files 1-2.pdf, 1-3.pdf, 2-3.pdf")

ax = fig.add_subplot(111)
# Plot the values
ax.scatter(x_vals, y_vals, c = cols, marker='x')
ax.set_xlabel('First Course Costs')
ax.set_ylabel('Second Course Costs')

plt.title("Clusters Visualization in 2d - 1st, 2nd Course")

plt.savefig("../Results/1-2.pdf")
ax.cla()

ax = fig.add_subplot(111)

# Plot the values
ax.scatter(y_vals, z_vals, c = cols, marker='x')
ax.set_xlabel('Second Course Costs')
ax.set_ylabel('Third Course Costs')
plt.title("Clusters Visualization in 2d - 2nd, 3rd Course")
plt.savefig("../Results/2-3.pdf")
ax.cla()

ax = fig.add_subplot(111)
# Plot the values
ax.scatter(x_vals, z_vals, c = cols, marker='x')
ax.set_xlabel('First Course Costs')
ax.set_ylabel('Third Course Costs')
plt.title("Clusters Visualization in 2d - 1st, 3rd Course")
plt.savefig("../Results/1-3.pdf")