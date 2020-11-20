#Written by "Shabnam Shahhoseyni"
#2020.11.13

# The problem is: 
# Pressures = 1 5 10 20 40 60 100 200 400 760
#Temperatures = -36.7 -19.6 -11.5 -2.6 7.6 15.4 26.1 42.2 60.6 80.1
# (a) Polynomial Regression P = a0 + a1T + a2T2 + a3T3 + ...+anTn
# (b) Regression Clausius_Clapeyron equation log(P)= A - (B / (T + 273.15))
# (c) nonlinear regression Antoine equation log(P)= a - (b / t + c))


# Introducing Variables:
# T = Temperature in C
# P = Pressure in mmHg

#Import Packages:
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
#from scipy.optimize import least_squares

#Input Data
print ('Enter the pressure values, Seperate each value by space')
p= input ()
Pressures = [float (x) for x in p.split ()]
Pressure_list = np.asarray (Pressures, dtype=np.float)
#Pressure_list = np.array ([1, 5, 10, 20, 40, 60, 100, 200, 400, 760])                          #for code test

print ('Enter the Temperature values, Seperate each value by space')
T= input ()
Temperatures = [float (x) for x in T.split ()]
Temperature_list = np.asarray (Temperatures, dtype=np.float)
#Temperature_list = np.array ([-36.7, -19.6, -11.5, -2.6, 7.6, 15.4, 26.1, 42.2, 60.6, 80.1])   #for code test

# Polynomial Regression (P = a0 + a1*T + a2*T**2 + a3*T**3 + ...+an*T**n)
def Calculate (n):
    Polynomial_Coefficients = np.polyfit (Temperature_list, Pressure_list, n , full=True)
    Polynomial_fit = np.polyval(Polynomial_Coefficients[0] ,Temperature_list)

    absError = Polynomial_fit - Pressure_list
    SE = np.square(absError)                                                                    # squared errors
    MSE = np.mean(SE)                                                                           # mean squared errors
    RMSE = np.sqrt(MSE)                                                                         # Root Mean Squared Error, RMSE
    Rsquared = 1.0 - (np.var(absError) / np.var(Pressure_list))
    return [Polynomial_Coefficients[0], RMSE, Rsquared, Polynomial_fit]

RMSEs=[]
for i in range (1, 10):
    outputs = Calculate (i)
    RMSEs.append(outputs[1])
    
n = RMSEs.index(min (RMSEs))
outputs = Calculate (n)

print ('Polynomial_Coefficients (highest power first):\n', outputs[0])
print ('The best polynomial degree = ', n)
print ('RMSE= ', outputs[1])
print ('R-squared= ', outputs[2])

plt.scatter (Temperature_list, Pressure_list)
plt.plot (Temperature_list, outputs[3], 'm')
plt.xlabel ('Temperature C')
plt.ylabel ('Pressure mmHg')
plt.title ('Pressure vs Temperature \nRegression')
plt.show ()

#Regression log(P)= A - (B / (T + 273.15))
def Clausius_Clapeyron (T, A, B):
    return 10**(A - (B / ( T + 273.15 )))

Coef, cov = curve_fit (Clausius_Clapeyron, Temperature_list, Pressure_list)

absError_CC = Clausius_Clapeyron (Temperature_list, Coef[0], Coef[1]) - Pressure_list
SE_CC = np.square(absError_CC)                                                                    # squared errors
MSE_CC = np.mean(SE_CC)                                                                           # mean squared errors
RMSE_CC = np.sqrt(MSE_CC)                                                                         # Root Mean Squared Error, RMSE
Rsquared_CC = 1.0 - (np.var(absError_CC) / np.var(Pressure_list))

print ('Clausius_Clapeyron Coefficients (A & B) = ', Coef)
print ('RMSE = ', RMSE_CC)
print ('Rsquared = ', Rsquared_CC )

plt.scatter (Temperature_list, Pressure_list)
plt.plot (Temperature_list, Clausius_Clapeyron (Temperature_list, Coef[0], Coef[1]), 'c')
plt.xlabel ('Temperature C')
plt.ylabel ('Pressure mmHg')
plt.title ('Pressure vs Temperature \nRegression for Clausius-Clapeyron equation')
plt.show ()

#nonlinear regression fitting log(P)= a - (b / t + c))
#def Antoine (t,a,b,c):
#    return 10**(a - (b / ( t + c )))

#Antoine_LS = least_squares(Antoine,[1,1,1,1])

#plt.scatter (Temperature_list, Pressure_list)
#plt.plot (Temperature_list, Antoine (Temperature_list, Coef2[0], Coef2[1], Coef2[2]), 'g')
#plt.xlabel ('Temperature C')
#plt.ylabel ('Pressure mmHg')
#plt.title ('Pressure vs Temperature \nRegression for Antoine equation')
#plt.show ()

print ('done')
