# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 12:42:28 2021

@author: hp
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2, linregress
from scipy.optimize import minimize  
from numpy import linalg as LA
  

#import our own files and reload
import file_function
importlib.reload(file_function)
import file_classes
importlib.reload(file_classes)

#inputs
inputs = file_classes.option_input()
inputs.volatility = 0.1442
inputs.interest_rate = 0.0158
inputs.maturity = 1 #in years
inputs.strike = 20
inputs.call_or_put = 'put'

radius = 0.10
inputs.price = np.linspace(1-radius,1+radius,1000) * inputs.strike
months = [0,3,6,9,11]
dict_plots = {}

# compute options prices
for month in months:
    # compute option price
    inputs.time = float(month) / (12 * inputs.maturity)
    price_black_scholes = file_function.compute_price_black_scholes(inputs)
    dict_plots[month] = price_black_scholes

# compute payoff
if inputs.call_or_put == 'call':
    payoff = np.array([max(s - inputs.strike, 0.0) for s in inputs.price])
elif inputs.call_or_put == 'put':
    payoff = np.array([max(inputs.strike - s, 0.0) for s in inputs.price])
    
# plot option prices
plt.figure()
plt.title('Plot of option prices | ' + inputs.call_or_put)
for month in months:
    plt.plot(inputs.price, dict_plots[month], label = str(month) + '-month')
plt.plot(inputs.price, payoff, label = 'payoff')
plt.ylabel('price option')
plt.xlabel('price underlying')
plt.legend()
plt.grid()
plt.show()



    
