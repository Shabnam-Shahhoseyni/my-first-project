# -*- coding: utf-8 -*-
"""
(a) Plot the conversion (X), reduced pressure (y) and temperature (T ´10-3) along the reactor
from W = 0 kg up to W = 20 kg.
(b) Around 16 kg of catalyst you will observe a “knee” in the conversion profile. Explain why this
knee occurs and what parameters affect the knee.
(c) Plot the concentration profiles for reactant A and product C from W = 0 kg up to W = 20 kg.

@author: shahh
"""
#------------------------------------------------------------------------------
# Rev 0.0
# Nov 19, 2020
# Note:
    

import numpy as np
from   scipy.integrate import solve_ivp 
import matplotlib.pyplot as plt 
from   scipy.optimize import fsolve

CPA = 40.0          # J/g-mol.K 
R = 8.314           # J/g-mol.K
CPC = 80.0          # J/g-mol.K 
FA0 = 5.0           # g-mol/min
dHR = - 40,000      # J/g-mol 
Ua  = 0.8           # J/kg.min.K
EA  = 41,800        # J/g-mol.K 
Ta  = 500           # K
k450   = 0.5        # dm6/kg×min×mol @ 450 K
a   = 0.015         # kg-1
KC450  = 25,000     # dm3/g-mol @ 450 K 
P0  = 10            # atm
CA0 = 0.271         # g-mol/dm3 
yA0 = 1.0           # (Pure A feed)
T0  = 450           # K

# part a-----------------------------------------------------------------------

def reac (v):
     T  = v[0]
     X  = v[1]
     P  = v[2]
     F = np.empty (6)
     k  = k450 * np.exp ((EA/R) * ((1/T0) - (1/T)))
     KC = KC450 * np.exp ((dHR/R) * ((1/T0) - (1/T)))
     y  = P/P0
     CA = CA0 * ((1-X)/(1-(0.5*X))) * y * (T0/T)
     CC = ((0.5 * CA0 * X)/ (1 - (0.5 * X))) * y * (T0/T)
     rA = (-k) * (CA**2 - CC/KC)
     return 
g = fsolve (reac, [450, 0, P0]) 
print (g)
# def reaction ( w,d):    # v: variables , d: differential equations 
#     # T  = v[0]
#     # X  = v[1]
#     # P  = v[2]

    
#     k  = k450 * np.exp ((EA/R) * ((1/T0) - (1/T)))
#     KC = KC450 * np.exp ((dHR/R) * ((1/T0) - (1/T)))
#     y  = P/P0
#     CA = CA0 * ((1-X)/(1-(0.5*X))) * y * (T0/T)
#     CC = ((0.5 * CA0 * X)/ (1 - (0.5 * X))) * y * (T0/T)
#     rA = (-k) * (CA**2 - CC/KC)
    
#     d = [0,0,0]
#     d[0] = -rA / FA0                                     # dXdW 
#     d[1] = ((-a * (1 - (0.5 * X))) / (2 * y)) * (T/T0)   # dydW 
#     d[2] = ((Ua * (Ta - T)) + (rA * dHR)) / (FA0 * CPA)  # dTdW 
#     return d

# d_first_stimation = [T0, 0,P0,0,0,0]     # initial condition [X0 , y0 , T0] 
# W = [0, 20]                         # catalyst weight
# ode_system = solve_ivp (reaction, W , d_first_stimation)

# # plot results
# plt.plot(ode_system["t"], ode_system["y"][0],'b')
# plt.title('Concentration per Distance graph')
# plt.xlabel('Distance (m)')
# plt.ylabel('Concentration (kg mol/m3)')
# plt.show()


# part c-----------------------------------------------------------------------
# Concentrations = []
# def concentration (z):
#     T  = z[0]
#     X  = z[1]
#     P  = z[2]
    
#     C = [[],[]]
#     C[0] = CA0 * ((1-X)/(1-(0.5*X))) * (P/P0) * (T0/T)
#     C[1] = ((0.5 * CA0 * X)/ (1 - (0.5 * X))) * (P/P0) * (T0/T)
#     return C
    
# initial_stimations = [T0, 0, P0]
# w = np.linspace (0, 20)
# for i in w:
#     Conc = fsolve(concentration, initial_stimations )
#     Concentrations.append [Conc]

# # plot results
# plt.plot(Concentrations[0], W,'b', Concentrations[1], W, 'r')
# plt.legend('CA', 'CC')
# plt.title('Concentration profile per Catalyst weight')
# plt.xlabel('Catalyst Weight kg')
# plt.ylabel('Concentration (kg mol/m3)')
# plt.show()



# def reaction ( w,d):    # v: variables , d: differential equations 
#     # T  = v[0]
#     # X  = v[1]
#     # P  = v[2]

    
#     k  = k450 * np.exp ((EA/R) * ((1/T0) - (1/T)))
#     KC = KC450 * np.exp ((dHR/R) * ((1/T0) - (1/T)))
#     y  = P/P0
#     CA = CA0 * ((1-X)/(1-(0.5*X))) * y * (T0/T)
#     CC = ((0.5 * CA0 * X)/ (1 - (0.5 * X))) * y * (T0/T)
#     rA = (-k) * (CA**2 - CC/KC)
    
#     d = [0,0,0]
#     d[0] = -rA / FA0                                     # dXdW 
#     d[1] = ((-a * (1 - (0.5 * X))) / (2 * y)) * (T/T0)   # dydW 
#     d[2] = ((Ua * (Ta - T)) + (rA * dHR)) / (FA0 * CPA)  # dTdW 
#     return d

# d_first_stimation = [T0, 0,P0,0,0,0]     # initial condition [X0 , y0 , T0] 
# W = [0, 20]                         # catalyst weight
# ode_system = solve_ivp (reaction, W , d_first_stimation)

# # # plot results
# # plt.plot(ode_system["t"], ode_system["y"][0],'b')
# # plt.title('Concentration per Distance graph')
# # plt.xlabel('Distance (m)')
# # plt.ylabel('Concentration (kg mol/m3)')
# # plt.show()



