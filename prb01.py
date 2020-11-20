#Written by "Shabnam Shahhoseyni"
#2020.11.12

# The problem has 3 parts: 
# (a) Calculate the molar volume and compressibility factor for gaseous ammonia at a pressure P = 56 atm and a temperature T = 450 K using the van der Waals equation of state.
# (b) Repeat the calculations for the following reduced pressures: Pr = 1, 2, 4, 10, and 20.
# (c) How does the compressibility factor vary as a function of Pr.?

# Introducing Variables:
# P = pressure in atm                                                
# V = molar volume in liters/g-mol                                   
# T = temperature in K                                               
# R = gas constant (R = 0.08206 atm.liter/g-mol.K)                   
# Tc = critical temperature (405.5 K for ammonia)                    
# Pc = critical pressure (111.3 atm for ammonia)
# Pr = reduced pressure
# Tr = Reduced temperature

# Import Packages 
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

# Variables value
R = 0.08206 
Tc = 405.5
Pc = 111.3
a = ( 27 / 64 ) * ( ( ( R**2 ) * ( Tc**2 ) ) / Pc )
b = ( R * Tc ) / ( 8 * Pc )

which_question = input ('Enter the question you want to solve: (a, b or c ?) ')

#Input pressure & temperature
T = int (input ("Enter T in K: "))

if which_question == 'a' :
    P = int( input ( "Enter P in atm: " ) )
    def wdv(v):    
        return ( ( ( P + ( a / v**2 ) ) * ( v - b ) ) - ( R * T ) )     # Wandervals Equation
    V = fsolve(wdv,[1])
    Z = ( P * V ) / ( R * T )                                           # Compresibility factor equation                                            
    
else :
    Pr = []
    V = []
    Z = []
    print ("Enter all of 'Pr' values (press enter after each value)")
    for i in range (1, 6):
        pr = int (input ())
        print ("\n")
        P = Pc * pr
        def wdv(v):    
            return ( ( ( P + ( a / v**2 ) ) * ( v - b ) ) - ( R * T ) ) # Wandervals Equation
        v = fsolve(wdv,[1])
        z = ( P * v ) / ( R * T )                                       # Compresibility factor equation  
        V.append (v)
        Z.append (z)
        Pr.append (pr)
        
# Printing answers:
print ("the molar volume for each Pr is: ", V)
print ("the compressibility factor for each Pr is: ", Z)

# Plot
if which_question == 'b' or which_question == 'c' :
    plt.plot ( Pr , Z )
    plt.xlabel ('Reduced Pressure (Pr)')
    plt.ylabel ('Compressibility Factor (Z)')
    plt.title ('Compressibility Factor vs Reduced Pressure (Z)')
    plt.show ()

print ("\ndone")