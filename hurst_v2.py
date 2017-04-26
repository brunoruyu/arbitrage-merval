# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:19:05 2016

@author: RY05295
"""
"""
with open('file.dat','r') as f:
    w, h = [int(x) for x in next(f).split()]
    array = [[int(x) for x in line.split()] for line in f]
"""
import numpy as np
import statsmodels.api as sm
import pandas

def linearfit (X,Y):
    X = sm.add_constant(X)
    model = sm.OLS(Y,X)
    results = model.fit()
    return results.params

#file_write = open('Hurst_total.dat', 'w')    
output = open('ParaFiteos.dat', 'w')    

file_handle = open('datos.dat', 'r')
# Read in all the lines of your file into a list of lines
lines_list = file_handle.readlines()
# Extract dimensions from first line. Cast values to integers from strings.
rows, cols = (int(val) for val in lines_list[0].split())
# Do a double-nested list comprehension to get the rest of the data into your matrix
ret = [[float(val) for val in line.split()] for line in lines_list[1:]]



Pais = cols  #cols=16
Tfin = rows  #rows=1200

#mean = np.ones((Pais)) 
Xt = np.ones((Tfin,Pais))
Yt = np.ones((Tfin,Pais))  
TimeVect = range(0,Tfin) 
B = np.ones(2) 

n=[10,20,30,50,100,200]
Fn = np.ones(6)
H = np.ones(Pais)

logn = np.ones(6)
logFn = np.ones(6)

#mean = [0] * rows

for j in range(0,Pais):
#for j in range(5,6):    #Loop sobre Pais
    mean=0.0
    
    for t in range(0,Tfin): #Loop en el tiempo para calcular valor medio
        mean += ret[t][j]/Tfin 
  
    #print(j, mean[j])
    Xt[0][j] = ret[0][j] - mean
    for t in range(1,Tfin): #Loop en el tiempo para calucular Xt
       Xt[t][j] = Xt[t-1][j] + (ret[t][j] - mean)
    
    for i in range(0,len(n)): #Loop en n para hacer los fiteos
        Cant=int(Tfin/n[i])
        for k in range(0,Cant):
            B= linearfit(TimeVect[k*n[i]:(k+1)*n[i]],Xt[k*n[i]:(k+1)*n[i],j])
            #print(n[i],k,B[0],B[1])
            #print(n[i],Cant)
        
            for t in range(k*n[i],(k+1)*n[i]):
                Yt[t][j]=B[0]+B[1]*t
        
        Fn[i]=0.0
        for t in range(0,Tfin):
            Fn[i] += (Xt[t][j]-Yt[t][j])**2

        Fn[i]=(Fn[i]/Tfin)**0.5
        
        logn = np.log(n)
        logFn = np.log(Fn)

        strj = str(j)
        strn = str(logn[i])
        strF = str(logFn[i])
        string = strj + " " + strn + " " + strF + "\n"
        #print(string)
        output.write(string)        
        
        
        #print(j,logn[i],logFn[i])
"""        
    Haux= linearfit(logn,logFn)
    H[j] =  Haux[1]
    strj = str(j)
    strH = str(H[j])
    string = strj + " " + strH + "\n"
    #print(string)
    file_write.write(string)
"""
        
#file_write.close()
output.close()
file_handle.close()        
        
    

      