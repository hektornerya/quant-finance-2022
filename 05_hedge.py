# -*- coding: utf-8 -*-
"""
Created on Mon May 17 17:22:23 2021

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

#import our own files and reload
import file_classes
importlib.reload(file_classes)
import file_function
importlib.reload(file_function)



# INPUTS
inputs = file_classes.hedge_input()
inputs.benchmark = '^STOXX50E' 
# inputs.security = 'ENI.MI' # Reuters Identification Codex
inputs.security = 'BBVA.MC' # Reuters Identification Codex
inputs.hedge_securities = ['BP.L','ENI.MI','RDSA.AS','RDSA.L','REP.MC','EQNR.OL','XOP']
# inputs.hedge_securities = ['EQNR.OL','REP.MC']
# inputs.hedge_securities = ['FP.PA','BP.L']
# inputs.hedge_securities = ['^GDAXI','^FCHI']
inputs.delta_portfolio = 10 # mn USD

# COMPUTations
hedge = file_classes.hedge_manager(inputs)  
hedge.load_betas() # get the betas for portfolio and hedgese all data in console
# hedge.compute()  # compute optimal hedge via CAPM
# # EXACT SOLUTION
# hedge.compute_exact()  # exact solution when N=2
# optimal_hedge_exact = hedge.optimal_hedge
# # NUMERICAL SOLUTION
hedge.compute(regularisation=0.01)  # numerical solution
hedge_delta = hedge.hedge_delta
hedge_beta_usd = hedge.hedge_beta_usd


# # inputs solution
# dimensions = len(inputs.hedge_securities)
# x = np.zeros([dimensions,1])
# portfolio_delta = hedge.delta_portfolio
# portfolio_beta = hedge.beta_portfolio_usd
# betas = hedge.betas
# regularisation = 0.1
# optimal_result = minimize(fun=file_function.cost_function_hedge, x0=x, args=(portfolio_delta, portfolio_beta, betas, regularisation))
# optimal_hedge = optimal_result.x
# hedge_delta = np.sum(optimal_hedge)
# hedge_beta_usd = np.transpose(betas).dot(optimal_hedge).item()
# print(optimal_result)


##############
# script
##############
#INPUT PARAMETERS
# benchmark = '^STOXX50E' 
# security = 'BBVA.MC' # Reuters Identification Codex
# hedge_securities = ['SAN.MC','REP.MC']
# delta_portfolio = 10 # mn USD

# #COMPUTE BETAS
# capm = file_classes.capm_manager(benchmark, security)
# capm.load_timeseries() 
# capm.compute() 
# beta_portfolio = capm.beta
# beta_portfolio_usd = beta_portfolio * delta_portfolio # mn USD

# # PRINT INPUT
# print('------')
# print('Input portfolio:')
# print('Delta mnUSD for ' + security + ' is ' + str(delta_portfolio))
# print('Beta for ' + security + 'vs ' + benchmark + ' is ' + str(beta_portfolio))
# print('Beta mnUSD for ' + security + ' vs ' + benchmark + ' is ' + str(beta_portfolio_usd))

# # COMPUTE BETAS FOR THE HEDGES
# shape = [len(hedge_securities),1]
# betas = np.zeros(shape)
# counter = 0
# print('------')
# print('Input hedges:')
# for hedge_security in hedge_securities:
#     capm = file_classes.capm_manager(benchmark, hedge_security)
#     capm.load_timeseries() 
#     capm.compute() 
#     beta = capm.beta
#     print('Beta for hedge[' + str(counter) + '] = ' + hedge_security + ' vs ' + benchmark + ' is ' + str(beta))
#     betas[counter] = beta
#     counter +=1
        
# # EXTRACT SOLUTION USING MATRIX ALGEBRA
# deltas = np.ones(shape)
# targets = -np.array([[delta_portfolio],[beta_portfolio_usd]])
# mtx = np.transpose(np.column_stack((deltas,betas)))
# optimal_hedge = np.linalg.inv(mtx).dot(targets)
# hedge_delta = np.sum(optimal_hedge)
# hedge_beta_usd = np.transpose(betas).dot(optimal_hedge).item()

# # PRINT RESULT
# print('------')
# print('Optimizacion result')
# print('------')
# print('Delta: ' + str(delta_portfolio))
# print('Beta USD: ' + str(beta_portfolio_usd))
# print('------')
# print('Hedge delta: ' + str(hedge_delta))
# print('Hedge beta: ' + str(hedge_beta_usd))
# print('------')
# print('Betas for hedge: ')
# print(betas)
# print('------')
# print('Optimal hedge: ')
# print(optimal_hedge)
# print('------')





# 1*S_1 + 1*S_2 = -delta_portfolio
# 1.4718*S_1 + 1.2322*S_2 = -beta_portfolio_usd