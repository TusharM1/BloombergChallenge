import pandas as pd
from matplotlib import pyplot as plt

## Test Data
x = [1,2,3,4,5,6]
y = [1,4,9,16,25,36]
z = [72,50,32,18,8,2]

## Plot Line Graph
#plt.plot(x,y)
#plt.plot(x,z)

## Set Graph and Axis Titles
plt.title("test plot")
plt.xlabel("this is the x-axis")
plt.ylabel("this is the y-and-z-axis")

## Set Graph Legend
plt.legend(["this is y","this is z"])

## Read in JSON file
sample_data = pd.read_json("SBHSData.json")

## Print JSON and data type
#print(sample_data)
#print(type(sample_data))

## Print JSON data column and type
#print(sample_data.uptime)
#print(type(sample_data.uptime))

## Retrive specific index value from data column
#print(sample_data.uptime.iloc[1])

# plt.plot(range(3033), sample_data.uptime)
set_xlim(0, max(sample_data.uptime))

## Show Graph
plt.show()