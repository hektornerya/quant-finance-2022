# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 13:33:22 2021

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
import file_classes
importlib.reload(file_classes)
import file_function
importlib.reload(file_function)


# universe
# rics = ['BARC.L','BBVA.MC','BNP.PA','CBK.DE','CSGN.SW','DBK.DE',\
#             'GLE.PA','HSBA.L','SAN.MC','UBSG.SW']
# rics = ['BP.L','ENI.MI','RDSA.AS','RDSA.L','EQNR.OL','REP.MC','XOP'] # OILS
# rics = ['SGRE.MC','VWS.CO','ORSTED.CO','FSLR','NEE']
# rics = ['^GSPC', '^VIX']
# rics = ['^FTSE','^GDAXI','^FCHI','^STOXX50E']
rics = ['CAD=X','CHF=X','CNY=X','EURUSD=X','GBPUSD=X',\
        'JPY=X','MXN=X','NOK=X','SEK=X'] 

# input params
notional = 300 # mnUSD
target_return = 0.015 # 0.01 0.04 0.36 0.6 0.05 0.015
include_min_variance=True

dict_portfolios = file_function.compute_efficient_frontier(rics, notional, target_return, include_min_variance)
