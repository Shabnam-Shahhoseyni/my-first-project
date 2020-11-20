# -*- coding: utf-8 -*-
"""
The problem statement:
Three tanks in series are presented. 
Each tank is initially filled with 1000 kg of oil at 20°C.
Saturated steam at a temperature of 250°C condenses within coils immersed in 
each tank. 
The oil is fed into the first tank at the rate of 100 kg/min and 
overflows into the second and the third tanks at the same flow rate. 
The temperature of the oil fed to the first tank is 20°C.
The tanks are well mixed so that the temperature inside the tanks is uniform
and the outlet stream temperature is the temperature within the tank.
For a particular tank, the rate at which heat is transferred to the oil from
the steam coil is given by the expression:

Q = UA(Tsteam – T)
 
UA = 10 kJ/min·°C  (the heat transfer coefficient)
T = temperature of the oil in the tank in 
Q = rate of heat transferred in kJ/min 
W = W1 = W2 = W3 (the mass flow rate to each tank remains at the same fixed value)
M = M1 = M2 = M3

For the first tank, the energy balance can be expressed by:
    
Accumulation = Input - Output
M * Cp * (dT1/dt) = W * Cp * T0 + U * A * (Tsteam-T1) - W * Cp * T1

T0=20 C
W1=100 kg/min
Cp= 2.0 KJ/kg
Determine the steady state temperatures in all three tanks. What time interval
will be required for T3 to reach 99% of this steady state value during startup?
@author: shahh
"""
#------------------------------------------------------------------------------
# Rev 0.0
# Nov 18, 2020
# Note:
    

from   scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 

# Problem data and parameters
T0 = 20       # C
W1 = 100      # kg/min
UA = 10       # kJ/min·°C
Tsteam = 250  # °C
Cp = 2        # kJ/kg.
W = 100       # kg/min
M = 1000      # kg


# function that returns dy/dt
def energy_balance (t, T):
    dTdt=[0,0,0]
    for i in range (0,3):
        if i == 0:
            dTdt [i] = (W * Cp * (T0 - T[i]) + (UA * (Tsteam - T[i]))) / (M * Cp)
        else:
            dTdt [i] = (W * Cp * (T[i-1] - T[i]) + (UA * (Tsteam - T[i]))) / (M * Cp)
    #dTdt = (W * Cp * (T0 - T) + (UA * (Tsteam - T))) / (M * Cp)
    return dTdt

# solve ODE
T_first_stimation = [20,20,20]     # initial condition
t = [0, 90]  #np.linspace(1, 5000)                            # time interval
T_list = solve_ivp (energy_balance, t , T_first_stimation)

# plot results
plt.plot(T_list["t"], T_list["y"][0],'r',T_list["t"], T_list["y"][1],'g',T_list["t"], T_list["y"][2],'c')
plt.title('Temperature per Time graph')
plt.legend(['First_Tank','Second_Tank','Third_Tank'])
plt.xlabel('time (min)')
plt.ylabel('Temperature (°C)')
plt.show()





 