
# Problem Statement:
# A simple force balance on a spherical particle reaching terminal
# velocity in a fluid is given by::
# vt=sqrt[(4*g*(rp-r)*Dp)/(3*CD*r)]

# The drag coefficient on a spherical particle at a terminal velocity
# varies with the Reynolds number(Re) as follows(pp 5-63, 5-64 in
# Perry):
# C_D=24/Re 	           	 for Re<0.1		
# C_D=24*(1+0.14Re^0.7)/Re   for 0.1<Re<1000	
# C_D=0.44 		             for 1000<Re<350000	
# C_D=0.19-80000/Re 	     for 350000<Re

# where Re = Dp*vt*r/mu

# (a) Calculate the terminal velocity for particles of coal
# (b) Estimate the terminal velocity of the coal particles in water within
# a centrifugal separator where the acceleration is 30.0g.


# vt : terminal velocity in m/s,
# g  : acceleration gravity given by 9.80665 m/s^2
# rp : particles density in kg/m^3
# r  : fluid density in kg/m^3 
# Dp : diameter of the spherical particle in m
# CD : dimensionless coefficient
# mu : viscosity in Pa*s

#------------------------------------------------------------------------------
# Rev 1.0
# Nov 14, 2020
# Note:
    
    
import numpy as np

# Problem data and parameters
rp = 1800			    # kg/m^3
Dp = 0.208 * (10**(-3))	# m
T = 298.15			    # K
r = 994.6 		    	# kg/m^3
mu = 8.931*(10**(-4))	# kg/m/s
g_1 = 9.80665 			# m/s^2
g_cent = 20 * g_1

# main function
def terminal_velocity (g):
    
    vt_guess = 5            # initial guess for vt
    delta = 1               # initial delta for begining the while loop 

    while delta == 1:
        Re = (Dp * vt_guess * r ) / mu

        if Re < 0.1:
            CD = 24 / Re
    
        elif Re <= 1000:
            CD = (24 / Re) * ((1 + 0.14) * Re**0.7)
    
        elif Re <= 35000:
            CD = 0.44
    
        else:
            CD = 0.19 - (8 * 10**4 / Re)

        vt = np.sqrt ((4 * g * (rp - r) * Dp) / (3 * CD * r))    

        if vt == vt_guess:
            delta = 0
        else:
            vt_guess = vt
      
    return (vt, Re ,CD)
# part a-----------------------------------------------------------------------

vt, Re ,CD = terminal_velocity(g_1)

print ('Results for part a: \n')
print ('Re =  ', Re)
print ('vt =  ', vt)
print ('CD =  ', CD)

print ('\n\n')
#part b-----------------------------------------------------------------------
vt2, Re2 ,CD2 = terminal_velocity(g_cent)

print ('Results for part b: \n')
print ('Re =  ', Re2)
print ('vt =  ', vt2)
print ('CD =  ', CD2)

print ('\n\ndone')