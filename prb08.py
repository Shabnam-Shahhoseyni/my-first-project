# -*- coding: utf-8 -*-
"""
For a binary batch distillation process involving two components designated 1 
and 2 (benzene(component 1) and toluene (component 2)) the moles of liquid
remaining, L, as a function of the mole fraction of the component 2, x2,
can be expressed by the following equation:

dL/dx2 = L/ (x2 * (k2 – 1))
ki = Pi / P 
Pi = 10^ (A - B/(T + C))
k1*x1 + k2*x2 = 1

k2 is the vapor liquid equilibrium ratio for component 2
Pi is the vapor pressure of component i 
P is the total pressure in mmHg
T is the temperature in °C.

The batch distillation of benzene (component 1) and toluene (component 2)
mixture is being carried out at
pressure of 1.2 atm.
Initially, there are 100 moles of liquid in the still,
comprised of 60% benzene and 40% toluene (mole fraction basis). 
Calculate the amount of liquid remaining in the still when concentration of
toluene reaches 80%.

A1 = 6.90565
B1 = 1211.033 
C1 = 220.79 
A2 = 6.95464
B2 = 1344.8 
C2 = 219.482 

@author: shahh
"""
#------------------------------------------------------------------------------
# Rev 1.0
# Nov 19, 2020
# Note:
    
import matplotlib.pyplot as plt
import numpy as np
from   scipy.optimize import fsolve
from   scipy.integrate import solve_ivp 

# Problem data and parameters
A = [6.90565, 6.95464]
B = [1211.033, 1344.8]
C = [220.79, 219.482]

Pt = 1.2 * 760  # atm
x = [0.6, 0.4]
x2_0 = 0.4
x2_end = 0.8
L0 = [100]

def vap_pressure (T):
    P = [[],[]]
    k = [[],[]]

    for i in range (0,2):
        P[i] = 10** (A[i] - B[i]/(T + C[i]))
        k[i] = P[i] / Pt 
        
    f = (k[0]*x[0] + k[1]*x[1]) - 1
    return f

T_initial_stimation = [(80.1+111)/2]   # benzene & toluene average boiling point

T=fsolve(vap_pressure,T_initial_stimation)
    
def remained_liquid (x, L):
    P = 10** (A[1] - B[1]/(T + C[1]))
    k = P / Pt 
    
    dLdx = L / (x * (k - 1))
    return dLdx

x = [x2_0, x2_end]
L_list = solve_ivp (remained_liquid, x ,L0)

plt.plot(L_list["t"], L_list["y"][0])
plt.title('Toluene Distilation graph')
plt.xlabel('X2')
plt.ylabel('Liquid remaining')
plt.show()







