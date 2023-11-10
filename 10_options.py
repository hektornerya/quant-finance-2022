# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 12:37:54 2021

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
inputs.price = 105
inputs.time = 0.0 #in years
inputs.volatility = 0.25
inputs.interest_rate = 0.01
inputs.maturity = 3/12 #in years
inputs.strike = 95
inputs.call_or_put = 'put'
number_simulations = 1*10**6

# price usin Black Sholes formula
price_black_sholes_put = file_function.compute_price_black_scholes(inputs)

# price using Monte Carlo simulations
prices_monte_carlo = file_function.compute_price_monte_carlo(inputs, number_simulations, inputs.call_or_put)
print(prices_monte_carlo)
prices_monte_carlo.plot_histogram()
