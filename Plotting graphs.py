#Exercise 1
#Plotting a linear graph
#The table below shows the number of days of pigs growth and their corresponding weight mesured in pounds within the 20 days period
#Make sure that you already have tabulate, matplotlib, numpy and pandas installed already. Use pip to install them if you have not.
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

Days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
Weight = [40.0,41.1,42.2,43.3,44.5,45.7,46.8,48.0,49.2,50.5,51.7,53.0,54.3,55.5,56.9,58.2,59.5,60.9,62.2,63.6]

print("TABLE 1")
table_1 = np.array([["Days", "Weight"],[1, 40.0],[2, 41.1],[3, 42.2],[4, 43.3],[5, 44.5],[6, 45.7],[7, 46.8],[8, 48.0],[9, 49.2],[10, 50.5],
                   [11, 51.7],[12, 53.0],[13, 54.3],[14, 55.5],[15, 56.9],[16, 58.2],[17, 59.5],[18, 60.9],[19, 62.2],[20, 63.6]])

table = pd.DataFrame(table_1)
newtable = table.transpose()
print(tabulate(newtable, tablefmt = "fancy_grid",showindex = False))

plt.plot(Days, Weight, c = "green", marker = 'o', markersize = 4, markerfacecolor = "blue")
plt.xlabel("Days of Pig Growth") 
plt.ylabel("Weight of Pig")
plt.title("Pig Growth Period")
plt.xticks(range(0, 22, 1))
plt.yticks(range(0, 100, 10))
plt.grid(True)
plt.show()
#From the graph plotted, it is evident that this is a linear graph due to it being a straight line, thus y=mx+c. 
#The gradient of this line is y2-y1/x2-x1 = 41.1-40/2-1 = 1.1.
#Thus, the equation of this line is y-40=1.1(x-1) = y=1.1x-1.1+40 = y=1.1x+38.9 


#Exercise 2
#Plotting a quadratic graph
#The table below shows records from RS Farms on the amount of sales he made by selling meat at the various freezer temperatures
Freezer_temp = [-23,-18,-15,-12,-10,-5,0,5, 10,15,20,23,25,27,30]
Sales = [120,100,90,85,80,75,0,65,55,50,40,20,15,10,5]

print("TABLE 2")
table_2 = np.array([["Freezer_Temp", "Sales"],[-23, 120],[-18, 100],[-15, 90],[-12, 85],[-10, 80],[-5, 75],[0,0],[5, 65],
                    [10, 55],[15, 50],[20, 40],[23, 20],[25, 15],[27, 10],[30, 5]])

data = pd.DataFrame(table_2)
newdata = data.transpose()
print(tabulate(newdata, tablefmt = "fancy_grid",showindex = False))

plt.plot(Freezer_temp, Sales, c = "brown", marker = '*', markersize = 6, markerfacecolor = "red")
plt.xlabel("Freezer temperature") 
plt.ylabel("Sales of meat")
plt.title("RS Farms' Record book")
plt.xticks(range(-25, 40, 5))
plt.yticks(range(0, 130, 10))
plt.grid(True)
plt.show()
#The graph plotted is a quadratic graphic at y = ax^2, with the point(0,0) being the minimum point.
#This indicates that a is positive
#The equation is y = a(x^2)


#Exercise 3
#Plotting the trigonometric identities
ϑ = [0,30,45,60,90,180,270]
cosϑ = [1, 0.87, 0.71, 0.50, 0, -1, 0]
sinϑ = [0, 0.5, 0.71, 0.87, 1, 0, -1]
tanϑ = [0, 0.58, 1, 1.73, "error", 0, "error"]

table_3 = {"ϑ" : [0,30,45,60,90,180,270], 
           "cosϑ" : [1, 0.87, 0.71, 0.50, 0, -1, 0], 
           "sinϑ" : [0, 0.5, 0.71, 0.87, 1, 0, -1], 
           "tanϑ": [0, 0.58, 1, 1.73, "error", 0, "error"]}

tab = pd.DataFrame(table_3)
newtab = tab.transpose()

print("TABLE 3")
print(tabulate(newtab, tablefmt = "fancy_grid"))

plt.plot(θ, cosθ, c = "green",marker = 'o', markersize = 5, markerfacecolor = "yellow", linewidth = 2, linestyle = '--', label = "cosθ" )
plt.plot(θ, sinθ, c = "blue", marker = '*', markersize = 8, markerfacecolor = "orange", linewidth = 2, linestyle = '-.', label = "sinθ" )
plt.plot(θ, tanθ, c = "red", marker = '^', markersize = 4, markerfacecolor = "blue", linewidth = 2, linestyle = ':', label = "tanθ")

plt.xlabel("θ") 
plt.ylabel("cosθ, sinθ, tanθ")
plt.title("Trigonometic Graphs")
plt.legend()
plt.grid(True)
plt.show()