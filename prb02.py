#Written by "Shabnam Shahhoseyni"
#2020.11.12

# The problem is: 
# Xylene, styrene, toluene and benzene are to be separated with the array of distillation columns, where D, B, D1, B1, D2 and B2 are the molar flow rates in mol/min.
# (a) Calculate the molar flow rates of streams D1, D2, B1 and B2.
# (b) Determine the molar flow rates and compositions of streams B and D.

# Introducing Variables:
# B = molar flow rate of stream B
# D = molar flow rate of stream D
# B1 = molar flow rate of stream B1
# D1 = molar flow rate of stream D1
# B2 = molar flow rate of stream B2
# D2 = molar flow rate of stream D2
# XBx = mole fraction of Xylene in stream B
# XBs = mole fraction of Styrene in stream B
# XBt = mole fraction of Toluene in stream B
# XBb = mole fraction of Benzene in stream B
# XDx = mole fraction of Xylene in stream D
# XDs = mole fraction of Styrene in stream D
# XDt = mole fraction of Toluene in stream D
# XDb = mole fraction of Benzene in stream Dno

#Import Packages:
import numpy as np

#Input Data
Q = input ('Do you want to input a new material balance? (yes/no)')

if Q == "yes" :
    Coefficients=[]
    print ('Enter the coefficients of material balance equations row by row')
    print ('Seperate 4 values of each row by space, then press enter for next row')
    for i in range (1, 5):
        n = input ()
        m = n.split ()                                                                  #Space delimited input row
        M = [float (x) for x in m]                                                      #Convert each ellement of input row to float
        Coefficients.append (M)
    
    
    print ('Enter the data vector of Material balance equations ')
    print ('Seperate 4 values by space ')
    k = input ()
    p = k.split ()                                                                     #Space delimited input row
    Right_side = [float (x) for x in p]                                                #Convert each ellement of input row to float
        
    Coefficients_matrix = np.asarray (Coefficients, dtype=np.float)                    #Convert Coefficients list to np.array
    Right_Side_matrix = np.asarray (Right_side, dtype=np.float)                        #Convert Right_side list to np.array
    
    Unknowns = np.dot (np.linalg.inv(Coefficients_matrix), Right_Side_matrix)          #Unknowns = [D1, B1, D2, B2]
    D1 = Unknowns [0]
    B1 = Unknowns [1]
    D2 = Unknowns [2]
    B2 = Unknowns [3]
    
    # Overall balances and individual component balances on column #2
    D = D1 + B1                                                                        #Molar Flow Rates

    XDx = (Coefficients_matrix[0,0] * D1 + Coefficients_matrix[0,1] * B1) / D          #Xylene
    XDs = (Coefficients_matrix[1,0] * D1 + Coefficients_matrix[1,1] * B1) / D          #Styrene
    XDt = (Coefficients_matrix[2,0] * D1 + Coefficients_matrix[2,1] * B1) / D          #Toluene
    XDb = (Coefficients_matrix[3,0] * D1 + Coefficients_matrix[3,1] * B1) / D          #Benzene
    
    # overall balances and individual component balances on column #3
    B = D2 + B2                                                                        #Molar Flow Rates

    XBx = (Coefficients_matrix[0,2] * D2 + Coefficients_matrix[0,3] * B2) / B          #Xylene
    XBs = (Coefficients_matrix[1,2] * D2 + Coefficients_matrix[1,3] * B2) / B          #Styrene
    XBt = (Coefficients_matrix[2,2] * D2 + Coefficients_matrix[2,3] * B2) / B          #Toluene
    XBb = (Coefficients_matrix[3,2] * D2 + Coefficients_matrix[3,3] * B2) / B          #Benzene
     
    
else :    
    # Material balances on individual components on the overall separation train
    # 0.07 * D1 + 0.18 * B1 + 0.15 * D2 + 0.24 * B2 = 0.15 * 70                        #Xylene
    # 0.04 * D1 + 0.24 * B1 + 0.10 * D2 + 0.65 * B2 = 0.25 * 70                        #Styrene
    # 0.54 * D1 + 0.42 * B1 + 0.54 * D2 + 0.10 * B2 = 0.40 * 70                        #Toluene
    # 0.35 * D1 + 0.16 * B1 + 0.21 * D2 + 0.01 * B2 = 0.20 * 70                        #Benzene

    Coefficients = np.array ( [[0.07, 0.18, 0.15, 0.24], [0.04, 0.24, 0.1, 0.65], [0.54, 0.42, 0.54, 0.1],[0.35, 0.16, 0.21, 0.01]])
    Right_side = np.array ([ 0.15*70 , 0.25*70 , 0.4*70 , 0.2*70])
    Unknowns = np.dot (np.linalg.inv(Coefficients), Right_side)                        #Unknowns = [D1, B1, D2, B2]
    D1 = Unknowns [0]
    B1 = Unknowns [1]
    D2 = Unknowns [2]
    B2 = Unknowns [3]

    # Overall balances and individual component balances on column #2
    D = D1 + B1                                                                        #Molar Flow Rates

    XDx = (0.07 * D1 + 0.18 * B1) / D                                                  #Xylene
    XDs = (0.04 * D1 + 0.24 * B1) / D                                                  #Styrene
    XDt = (0.54 * D1 + 0.42 * B1) / D                                                  #Toluene
    XDb = (0.35 * D1 + 0.16 * B1) / D                                                  #Benzene

    # overall balances and individual component balances on column #3
    B = D2 + B2                                                                        #Molar Flow Rates

    XBx = (0.15 * D2 + 0.24 * B2) / B                                                  #Xylene
    XBs = (0.10 * D2 + 0.65 * B2) / B                                                  #Styrene
    XBt = (0.54 * D2 + 0.10 * B2) / B                                                  #Toluene
    XBb = (0.21 * D2 + 0.01 * B2) / B                                                  #Benzene


# Printing answers
print ('molar flow rate of stream D1: ', D1)
print ('molar flow rate of stream D2: ', D2)
print ('molar flow rate of stream B1: ', B1)
print ('molar flow rate of stream B2: ', B2)

print ('molar flow rates of stream B: ', B)
print ('molar flow rates of stream D: ', D)
print ('mole fraction of Xylene in stream B: ', XBx)
print ('mole fraction of Styrene in stream B: ', XBs)
print ('mole fraction of Toluene in stream B: ', XBt)
print ('mole fraction of Benzene in stream B: ', XBb)
print ('mole fraction of Xylene in stream D: ', XDx)
print ('mole fraction of Styrene in stream D: ', XDs)
print ('mole fraction of Toluene in stream D: ', XDt)
print ('mole fraction of Benzene in stream D: ', XDb)

print ('\ndone')