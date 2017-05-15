# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:56:34 2017

@author: bruno
"""


import numpy as np
import statsmodels.api as sm
import pandas as pd

def linearfit (X,Y):
    X = sm.add_constant(X)
    model = sm.OLS(Y,X)
    results = model.fit()
    return results.params

ID1=40   
ID2=39
ID3=69 
    
file_write = open('Salida.dat', 'w')    
  
file_handle = open('datos_test.dat', 'r')
# Read in all the lines of your file into a list of lines
lines_list = file_handle.readlines()
#read = [[float(val) for val in line.split()] for line in lines_list[0:]]
read = []
for line in lines_list[0:]:
    if "NaN" not in line: 
        #str_lst = line.split()
        #float_lst=[float(x) for x in str_lst]
        float_lst = [float(x) for x in line.split()]
        read.append(float_lst)
       
       
matriz=np.array(sorted(read, key=lambda x : x[1]))
print(matriz)

ult = len(matriz[:])
print(ult)
T0=matriz[0][1]
Tf=matriz[ult-1][1]
print(Tf)

serie1= [] #va a ser una matriz con Tiempo en la primer columna, bid en la 2da, ask en la 3ra y el promedio en la 4ta
serie2= []
serie3= []

print(matriz[:0])


for i in range(0,ult):
    if matriz[i][0]==ID1:
        serie1.append([matriz[i][1],matriz[i][2],matriz[i][3],(matriz[i][2]+matriz[i][3])/2])
    elif matriz[i][0]==ID2:
        serie2.append([matriz[i][1],matriz[i][2],matriz[i][3],(matriz[i][2]+matriz[i][3])/2])
    elif matriz[i][0]==ID3:
        serie3.append([matriz[i][1],matriz[i][2],matriz[i][3],(matriz[i][2]+matriz[i][3])/2])


#No está tan bien...debería hacer uno solo donde estén todos los tiempos        
        
serie1=np.array(serie1)
serie2=np.array(serie2)
serie3=np.array(serie3)
print(serie2)    





"""

TimeVect = range(0,Tfin) 
B = np.ones(2) 

div = int(input("Ingrese cantidad de ruedas en cada ventana: "))
#div = 1
print("Ingrese los valores de n (separados por un espacio)")
n = [int(x) for x in input().split()]
#n=[10,20,30,50,100,200]

Fn = np.ones(len(n))
H = np.ones(Pais)

logn = np.ones(len(n))
logFn = np.ones(len(n))


cajas = int(Tfin/div)
Tfines = np.ones(cajas)
Tinic = np.ones(cajas)  
retcaja = np.ones(div)

Xt = np.ones(div)
Yt = np.ones(div)  #mean = [0] * rows

for j in range(0,Pais):
    #Loop sobre Pais
    

    for caj in range(0,cajas): #Loop para setear distintos bloques de tiempo
        Tinic=caj*div
        Tfines = (caj+1)*div
        mean=0.0
        
        p=0
        for t in range(Tinic,Tfines): #Loop en el tiempo para calcular valor medio
            retcaja[p] = ret[t][j]
            mean += retcaja[p]/div 
            p += 1 
              
        Xt[0] = retcaja[0] - mean
        
        for p in range(1,div): #Loop en el tiempo para calucular Xt
           Xt[p] = Xt[p-1] + (retcaja[p] - mean)
          
  
        for i in range(0,len(n)): #Loop en n para hacer los fiteos
           
            Cant=int(div/n[i])
            for k in range(0,Cant):
                B= linearfit(TimeVect[k*n[i]:(k+1)*n[i]],Xt[k*n[i]:(k+1)*n[i]])
                #print(n[i],k,B[0],B[1])
                #print(n[i],Cant)
            
                for p in range(k*n[i],(k+1)*n[i]):
                    Yt[p]=B[0]+B[1]*p
            
            Fn[i]=0.0
            for p in range(0,div):
                Fn[i] += (Xt[p]-Yt[p])**2
    
            Fn[i]=(Fn[i]/div)**0.5
            
        logn = np.log(n)
        logFn = np.log(Fn)

        Haux= linearfit(logn,logFn)
        H[j] =  Haux[1]
        strcaj = str(caj)
        strj = str(j)
        strH = str(H[j])
        string = strj + " " + strcaj + " " + strH + "\n"
        #print(string)
        file_write.write(string)

file_write.close()
file_handle.close() 
#output.close()       


"""