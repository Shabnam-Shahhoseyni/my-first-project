# -*- coding: utf-8 -*-
"""

@author: shahh
"""
#------------------------------------------------------------------------------
# Rev 0.0
# Nov 26, 2020
# Note:
    

import numpy as np
from   scipy.integrate import solve_ivp 
import matplotlib.pyplot as plt 

# variables and data parameters

rVCp = 4000  # kJ/°C 
WCp  = 500   # kJ/min°C
Tis  = 60    # °C        steady state design temperature
Tr   = 80    # °C        set point
td   = 1     # min       dead time
tm   = 5     # min       thermocouple time constant
tI   = 2     # min       integral time constant or reset time.
Kc   = int(input('Enter proportional gain = '))   

# defining the ODE system function
def Heated_Tank (t, T):    # time , T= Tempretures
    Tt     = T[0]          # Tank temperature
    T0     = T[1]          # The temperature input to the thermocouple
    Tm     = T[2]          # Outlet temperature measured by thermocuple
    errsum = T[3]          # error
    
    if t < 10:             # the condition menssioned in part a
        Ti = 80
    else:
        Ti = 40
    
    qs = WCp * (Tr-Tis)
    q  = qs + Kc*(Tr-Tm) + ((Kc/tI)*(errsum))
    
    Temps = [[],[],[],[]]
    Temps[0] = (WCp * (Ti-Tt) + q) / (rVCp)    # dTdt
    Temps[1] = (Tt-T0-(td/2)*Temps[0])*(2/td)  # dT0dt
    Temps[2] = (T0 - Tm) / tm                  # dTmdt
    Temps[3] = (Tr - Tm)                       # d(errsum)dt
    return Temps

# part a-----------------------------------------------------------------------

t_span = [0, 200]
T_initial = [Tr,Tr,Tr,0]

solution= solve_ivp(Heated_Tank, t_span, T_initial ,dense_output=True)

t = np.linspace(0, 200, 200)
Temperatures = solution.sol(t)

plt.plot(t, Temperatures[0,:],'c')
plt.plot(t, Temperatures[1,:],'r')
plt.plot(t, Temperatures[2,:],'b')
plt.title('Temperature vs Time graph')
plt.xlabel('Time, min')
plt.ylabel('Temperature, °C')
plt.legend(['Tank','Outlet', 'Measured'])
# part b-----------------------------------------------------------------------






