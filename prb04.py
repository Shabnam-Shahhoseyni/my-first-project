
# The Problem is to solve this system of nonlinear algebraic equations:
# A + B <-> C + D
# B + C <-> X + Y
# A + X <-> Z
# KC1 = Cc*Cd/Ca*Cb
# KC2 = Cx*Cy/Cb*Cc
# KC3 = Cz/Ca*Cx
# Ca = Ca0 – Cd – Cz 
# Cb = Cb0 – Cd – Cy
# Cc = Cd – Cy 
# Cy = Cx + Cz


# CA, CB, CC, CD, CX, CY and CZ: concentrations of the various species
# CA0 and  CB0: initial concentrations
# KC1, KC2 & KC3: equilibrium constants
#------------------------------------------------------------------------------
# Rev 1.0
# Nov 14, 2020
# Note:


import numpy as np
from   scipy.optimize import fsolve  

# Problem data and parameters
Ca0 = Cb0 = 1.5
KC1 = 1.06
KC2 = 2.63
KC3 = 5

# Initial stimation function
def initial_stimation (CGuess):
    initials = np.empty (7)                     # Producing initial stimation array
    initials[0] = Ca0 - CGuess - CGuess         # initial stimation for CA
    initials[1] = CGuess + CGuess               # initial stimation for CY
    initials[2] = Cb0 - CGuess - initials[1]    # initial stimation for Cb
    initials[3] = CGuess - initials[1]          # initial stimation for Cc
    initials[4] = CGuess                        # initial stimation for CD
    initials[5] = CGuess                        # initial stimation for CX
    initials[6] = CGuess                        # initial stimation for CZ
    return initials

# main function
def Functions (C):
    Ca = C[0]
    Cy = C[1]
    Cb = C[2]
    Cc = C[3]
    Cd = C[4]
    Cx = C[5]
    Cz = C[6]
        
    F = np.empty (7)
    F[0] = (KC1 * Ca * Cb) - (Cc * Cd)
    F[1] = (KC2 * Cb * Cc) - (Cx * Cy )
    F[2] = (KC3 * Ca * Cx) - Cz
    F[3] = Ca0 - Cd - Cz - Ca
    F[4] = Cx + Cz - Cy
    F[5] = Cb0 - Cd - Cy - Cb
    F[6] = Cd - Cy - Cc
    return F

# part a-----------------------------------------------------------------------
Initial_Stimation0 = initial_stimation (0)
C1 = fsolve (Functions, Initial_Stimation0)

#part b------------------------------------------------------------------------
Initial_Stimation1 = initial_stimation (1)
C2 = fsolve (Functions, Initial_Stimation1)

#part c------------------------------------------------------------------------
Initial_Stimation10 = initial_stimation (10)
C3 = fsolve (Functions, Initial_Stimation10)


# Printing results
np.set_printoptions(precision=4) # for pretty print

print ('Results for part a :\n')
print ('CA = ', C1[0])
print ('CB = ', C1[2])
print ('CC = ', C1[3])
print ('CD = ', C1[4])
print ('CX = ', C1[5])
print ('CY = ', C1[1])
print ('CZ = ', C1[6])

print ('\n\n')

print ('Results for part b :\n')
print ('CA = ', C2[0])
print ('CB = ', C2[2])
print ('CC = ', C2[3])
print ('CD = ', C2[4])
print ('CX = ', C2[5])
print ('CY = ', C2[1])
print ('CZ = ', C2[6])

print ('\n\n')

print ('Results for part c :\n')
print ('CA = ', C3[0])
print ('CB = ', C3[2])
print ('CC = ', C3[3])
print ('CD = ', C3[4])
print ('CX = ', C3[5])
print ('CY = ', C3[1])
print ('CZ = ', C3[6])

print ('\ndone')

