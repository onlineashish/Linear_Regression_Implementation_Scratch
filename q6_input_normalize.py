# -*- coding: utf-8 -*-
"""Q6_input_normalize.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f7kCUuDOHfftApIrWG1t-OUn2FVdaxeV
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from linearRegression.linear_regression import LinearRegression
import os.path
from os import path

#TODO : Write here
if not path.exists('Plots/Question6/'):
    os.makedirs('Plots/Question6/')

x = np.array([i*np.pi/180 for i in range(60,300,2)])
y = 3*x + 8 + np.random.normal(0,3,len(x))

# Reshape x to a 2D array for sklearn
# X = x.reshape(-1, 1)
X = pd.DataFrame(x)
y = pd.Series(y)
X1 = X[:]
print(X.shape)
print(y.shape)
# Standardize the data using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled)
X_scaled1 = X_scaled[:]
print(X_scaled.shape)

# Fit a linear regression model on unnormalized data
lr_unscaled = LinearRegression()
lr_unscaled.fit_normal_equations(X, y)
y_pred_unscaled = lr_unscaled.predict(X)

# Calculate the mean squared error on unnormalized data
mse_unscaled = mean_squared_error(y, y_pred_unscaled)

# Fit a linear regression model on normalized data
lr_scaled = LinearRegression()
lr_scaled.fit_normal_equations(X_scaled, y)
y_pred_scaled = lr_scaled.predict(X_scaled)

# Calculate the mean squared error on normalized data
mse_scaled = mean_squared_error(y, y_pred_scaled)


# Plot the data and regression lines
#X = X.to_numpy()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.scatter(X1, y)
ax1.plot(X1, y_pred_unscaled, color='r')
ax1.set_title(f'Unnormalized Data (MSE={mse_unscaled:.2f})')

ax2.scatter(X_scaled1, y)
ax2.plot(X_scaled1, y_pred_scaled, color='r')
ax2.set_title(f'Normalized Data (MSE={mse_scaled:.2f})')

plt.savefig("Plots/Question6/fig.png")
plt.close()