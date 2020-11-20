# -*- coding: utf-8 -*-
"""
Problem Statement:
The diffusion and simultaneous first order irreversible chemical reaction in a single phase containing
only reactant A and product B results in a second order ordinary differential equation given by

d^2CA/dz^2 = (k/DAB) * CA

CA is the concentration of reactant A (kg mol/m3)
z is the distance variable (m),
k is the homogeneous reaction rate constant (s-1) 
DAB is the binary diffusion coefficient (m2/s).

Thus the initial and boundary conditions are:
CA = CA0     for  z = L
dCA/dz = 0   for  z = L

This differential equation has an analytical solution given by:
    
CA = (CA0 * (cosh (L * (sqrt k/DAB) (1 – z/L)))) / (cosh(L * sqrt (k/DAB)))

(a) Numerically solve Equation (23) with the given boundary conditions.
This solution should utilized an ODE solver with a shooting technique and employ Newton’s method or
some other technique for converging on the boundary condition given by Equation (25).

(b) Compare the concentration profiles over the thickness as predicted by the numerical solution
of (a) with the analytical solution of Equation (26).

CA0 = 0.2 kg mol/m3
k = 10^-3 s-1
DAB = 1.2 * 10^-9 m2/s
L = 10^-3 m.
This is a temporary script file.
"""
#------------------------------------------------------------------------------
# Rev 0.0
# Nov 19, 2020
# Note:
    
import numpy as np
from scipy.optimize import fsolve
from   scipy.integrate import solve_ivp 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

# Problem data and parameters
CA0 = 0.2              # kg mol/m3
k   = 10**-3           # s-1
DAB = 1.2 * 10**-9     # m2/s
L   = 10**-3           # m

# part a ----------------------------------------------------------------------

# Modification for Solution 
# breaking the (d2CA/dz2 = (k/DAB) * CA) equation to two first ODE:
# dCA/dz = w
# d2CA/dz2 = dw/dz

# def consentration ( z,C):
#     CA = C[0]
#     dCA = C[1]
    
#     Cdot = [[],[]]
#     Cdot[0] = dCA
#     Cdot[1] = (k/DAB) * CA
#     return Cdot
    
# # solve ODE
# C_first_stimation = [CA0,0]                                     # initial condition
# z = [0,L]                     # time interval
# C_list = solve_ivp (consentration, z , C_first_stimation)

def consentration ( C,z):
    CA = C[0]
    dCA = C[1]
    
    Cdot = [[],[]]
    Cdot[0] = dCA
    Cdot[1] = (k/DAB) * CA
    return Cdot
    
# solve ODE
z = np.linspace(0, L, 200)

C_first_stimation = [CA0,0]                                     # initial condition
C_list = odeint (consentration,  C_first_stimation,z)


# part b ----------------------------------------------------------------------


CA_analitical=[]
Z = np.linspace (0 , L)     
for i in Z:
    CA_a = (CA0 * (np.cosh (L * (np.sqrt (k/DAB)) * (1 - (i/L))))) / (np.cosh (L * np.sqrt (k/DAB)))
    CA_analitical.append (CA_a)

# plot results
plt.plot(z, C_list[:,0],'b',  Z , CA_analitical,'r')
plt.title('Concentration per Distance graph')
plt.xlabel('Distance (m)')
plt.ylabel('Concentration (kg mol/m3)')
plt.show()







