from os import name
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
cars_data = pd.read_csv('C:/Users/vishwaranjan/Desktop/Analyst Project/Project 2/cars.csv')

# Data Cleaning

cars_data = cars_data.dropna(how='all')

# filling the null data with before values
cars_data = cars_data.fillna(method='pad')

# data cleaned

Total_Makers = cars_data['Make'].value_counts()

#plotting graphs

# (1) plotting graph between car producing companies with respect to cars they produced

Car_makers = []
Numbers = []
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
for i in Total_Makers:
    Numbers.append(i)
for i in Total_Makers.index:
    Car_makers.append(i)
    
    
index_of_makers = [a for a in range(len(Numbers))]

plt.subplot(1,2,1)

plt.barh(index_of_makers,Numbers,0.8,color=['b','r','g','m','c'])

plt.xlabel('Total No. of Car Produced',color = 'b',fontdict=font1)
plt.ylabel('Car Producing Company',color='g',fontdict=font2)

plt.yticks(index_of_makers,Car_makers)

plt.title('Representation of No. of car produced from each Company')
for i in range(len(Numbers)):
    plt.text(Numbers[i],index_of_makers[i],Numbers[i])

# (2) plotting graph between no. of cylinders cars are using

cylinders = cars_data['Cylinders'].value_counts()
x= [int(i) for i in cylinders.index]
y = [int(i) for i in cylinders]

plt.subplot(1,2,2)
plt.bar(x,y,color=['r','m','b'])
plt.xlabel("No. of Cylinders",fontdict=font2)
plt.ylabel("Number of Cars",fontdict=font1)
plt.title("Showing Cars with Given Cylinders",color='b')
for i in range(len(y)):
    plt.text(x[i],y[i],y[i],ha='center',color='g')

plt.show()
#(3) Continent Wise Car Produced
continents = cars_data['Origin'].value_counts()

name_of_continent = [a for a in continents.index]
number_of_car_produced_in_continents = [a for a in continents]
plt.subplot(1,2,1)
plt.pie(number_of_car_produced_in_continents,labels=name_of_continent,colors=['y','r','b'],startangle=120,autopct='%1.1f%%')
plt.title("Continent Wise Car Production ")

#(4) Type of Car produced

car_produced = cars_data['Type'].value_counts()
name_of_car = [a for a in car_produced.index]
number_of_car = [a for a in car_produced]
index_of_car = [a for a in range(len(number_of_car))]

plt.subplot(1,2,2)

plt.barh(index_of_car,number_of_car,0.5,color=['y','r','b','m'])

plt.yticks(index_of_car,name_of_car)
plt.xlabel('Number of Cars',fontdict=font1)
plt.ylabel('Type of Car',fontdict=font2)
plt.title('Type of Cars and their Quantities',fontdict=font1)
for i in range(len(number_of_car)):
    plt.text(number_of_car[i],index_of_car[i],number_of_car[i])

plt.show()

