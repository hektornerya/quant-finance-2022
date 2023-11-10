# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:32:25 2021

@author: hp
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import scipy
import importlib
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis, chi2    

#import our own files and reload
import file_classes
importlib.reload(file_classes)

inputs = file_classes.distribution_input()
inputs.data_type = 'real'
inputs.variable_name = '^VIX'
inputs.degrees_freedom = 9
inputs.nb_sims = 10**6


dm = file_classes.distribution_manager(inputs)  #initialize consructor
dm.load_timeseries() #get de time series
dm.compute()  # compute returns and all different risk metrics
dm.plot_histogram() # plot histogram
print(dm) # write all data in console

