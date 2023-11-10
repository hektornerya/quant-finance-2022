# -*- coding: utf-8 -*-
"""
Created on Thu May  6 13:05:54 2021

@author: hp
"""


import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2, linregress    

#import our own files and reload
import file_classes
importlib.reload(file_classes)
import file_function
importlib.reload(file_function)

# inputs
benchmark = '^STOXX50E' # variable x
security = 'ENI.MI' # variable y

capm = file_classes.capm_manager(benchmark, security)  #initialize consructor
capm.load_timeseries() #get de time series
capm.plot_timeseries()
capm.compute()  # compute returns and all different risk metrics
capm.plot_linear_regression() # plot histogram
print(capm) # write all data in console



# # load 2 timeseries
# table_x = file_function.load_timeseries(benchmark)
# table_y = file_function.load_timeseries(security)

# load synchronised timeseries
# t = file_function.load_synchronised_timeseries(ric_x=benchmark, ric_y=security)



# # PLOT 2 TIMERIES WITH 2 VERTICAL AXES
# plt.figure(figsize=(12,5))
# plt.title('Timeseries of prices')
# plt.xlabel('Time')
# plt.ylabel('Preices')
# ax = plt.gca()
# ax1 = t.plot(kind='line', x='date', y='price_x', ax=ax, grid=True,\
#              color='blue', label=benchmark)
# ax2 = t.plot(kind='line', x='date', y='price_y', ax=ax, grid=True,\
#              color='red', secondary_y=True, label=security)
# ax1.legend(loc=2)
# ax2.legend(loc=1)
# plt.show()


# # LINEAR REGRESSION
# x = t['return_x'].values
# y = t['return_y'].values
# slope, intercept, r_value, p_value, std_err = linregress(x,y)
# nb_decimals = 4
# slope = np.round(slope, nb_decimals)
# intercept = np.round(intercept, nb_decimals)
# p_value = np.round(p_value, nb_decimals)
# null_hypothesis = p_value > 0.05 # p_value < 0.05 --> reject null hiypothesis
# r_value = np.round(r_value, nb_decimals) # correlation coefficient
# r_squared = np.round(r_value**2, nb_decimals) # pct of a variance of y explained by x
# predictor_linreg = intercept + slope*x

# # scatter plot returns
# str_title = 'Scaterplot of returns' + '\n'\
#     + 'linnear regression / security ' + security\
#     + ' / benchmark ' + benchmark + '\n'\
#     + 'alpha (intercept) ' + str(intercept)\
#     + ' / beta (slope) ' + str(slope) + '\n'\
#     + 'p-value' + str(p_value)\
#     + ' / null hypothesis ' + str(null_hypothesis) + '\n'\
#     + 'r-value (correl) ' + str(r_value)\
#     + ' / r-squared ' + str(r_squared)
# plt.figure()
# plt.title(str_title)
# plt.scatter(x,y)
# plt.plot(x, predictor_linreg, color='green')
# plt.ylabel(security)
# plt.xlabel(benchmark)
# plt.grid()
# plt.show()

    


# #synchronize timestamps
# timestamps_x = list(table_x['date'].values)
# timestamps_y = list(table_y['date'].values)
# timestamps = list(set(timestamps_x) & set(timestamps_y))

# #synchronised time series for benchmark
# table_x_sync = table_x[table_x['date'].isin(timestamps)]
# table_x_sync.sort_values(by='date', ascending=True)
# table_x_sync = table_x_sync.reset_index(drop=True)

# #synchronised time series for security
# table_y_sync = table_y[table_y['date'].isin(timestamps)]
# table_y_sync.sort_values(by='date', ascending=True)
# table_y_sync = table_y_sync.reset_index(drop=True)
    
# #table of return for ric and benchmark
# t = pd.DataFrame()
# t['date'] = table_x_sync['date']
# t['price_x'] = table_x_sync['close']
# t['return_x'] = table_x_sync['return_close']
# t['price_y'] = table_y_sync['close']
# t['return_y'] = table_y_sync['return_close']

# return t

# LINEAR REGRESSION
