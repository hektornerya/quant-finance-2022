# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:53:03 2021

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

notional = 300 # mnUSD

# rics = ['BARC.L','BBVA.MC','BNP.PA','CBK.DE','CSGN.SW','DBK.DE',\
#             'GLE.PA','HSBA.L','SAN.MC','UBSG.SW','XLF']
# rics = ['BARC.L','BNP.PA','XLF']    
# rics = ['^GSPC','^VIX'] # RENEWABLES USA
# rics = ['BP.L','ENI.MI','RDSA.AS','RDSA.L','EQNR.OL','REP.MC','XOP'] # OILS
rics = ['SGRE.MC','VWS.CO','ORSTED.CO','FSLR','NEE']

port_mgr = file_classes.portfolio_manager(rics, notional)
port_mgr.compute_covariance_matrix(bool_print=True)

port_min_var = port_mgr.compute_portfolio('min-variance')
port_min_var.summary()

port_min_var_l1 = port_mgr.compute_portfolio('min-variance-l1')
port_min_var_l1.summary()

port_min_var_l2 = port_mgr.compute_portfolio('min-variance-l2')
port_min_var_l2.summary()

port_long_only = port_mgr.compute_portfolio('long-only')
port_long_only.summary()

port_pca = port_mgr.compute_portfolio('pca')
port_pca.summary()

port_equi = port_mgr.compute_portfolio('equi-weight')
port_equi.summary()

port_volatility = port_mgr.compute_portfolio('volatility-weighted')
port_volatility.summary()

port_markowitz = port_mgr.compute_portfolio('markowitz', target_return=0.34)
port_markowitz.summary()


# # MIN-VARIANCE PORTFOLIO
# print('----') 
# print('Min-variance portfolio:')
# print('notional (mnUSD) = ' + str(notional))
# variance_explained = port_mgr.eigenvalues[0] / sum(abs(port_mgr.eigenvalues))
# eigenvector = port_mgr.eigenvectors[:,0]
# port_min_var = notional * eigenvector / sum(abs(eigenvector))
# delta_min_var = sum(port_min_var)
# print('delta (mnUSD) = ' + str(delta_min_var))
# print('variance explained = ' + str(variance_explained))

# # PCA (max-variance) PORTFOLIO
# print('----') 
# print('PCA portfolio (max-variance):')
# print('notional (mnUSD) = ' + str(notional))
# variance_explained = port_mgr.eigenvalues[-1] / sum(abs(port_mgr.eigenvalues))
# eigenvector = port_mgr.eigenvectors[:,-1]
# port_pca = notional * eigenvector / sum(abs(eigenvector))
# delta_pca = sum(port_pca)
# print('delta (mnUSD) = ' + str(delta_pca))
# print('variance explained = ' + str(variance_explained))



