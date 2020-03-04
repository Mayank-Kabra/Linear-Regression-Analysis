#importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

#Retireving data from CSV file
data = pd.read_csv(os.getcwd()+"/Housing Price data set.csv")
data.head()

#Adding the Bias Term
data.insert(0, 'bias', np.ones(len(data)))

#Getting required data for analysis
X = data[['bias', 'lotsize']]
Y = data['price']

#Normal Equation to find W (Training Model)
W = np.linalg.inv(X.T @ X) @ X.T @ Y
print("The weights are :")
print(W)

#Making Predictions using the trained model
ypred = [(W[0] + W[1]*lotsize) for lotsize in X['lotsize']]

#Plotting the Graph
plt.scatter(X['lotsize'], Y)
plt.plot(X['lotsize'], ypred, 'r')
plt.xlabel("LotSize")
plt.ylabel("Price of the House")

#Custom prediction based on lotsize
lotsize = int(input("Input LotSize  "))
prediction = W[0] + W[1]*lotsize
print('House of price is ', prediction)
