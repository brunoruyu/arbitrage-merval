# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:47:46 2017

@author: bruno
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import ReadData
import dinamica
import pandas as pd

ID0,ID1=39,69   
tinic,tfin="2016-10-03 12:09:46","2016-12-29 17:05:51"
Cinic=0


(dif,bid,ask)=ReadData.ReadCsv('data_IMERV.dat',ID0,ID1,tinic,tfin)
#df=ReadData.ReadExcel('data_I.MERV.xlsx')
#df=ReadData.ReadExcel('test.xlsx',ID1,ID2)
#df=ReadData.ReadCsv('test.dat',ID1,ID2)
dif=dif.drop('Act0', 1)
dif=dif.drop('Act1', 1)

ndif=np.array(dif)
nbid=np.array(bid)
nask=np.array(ask)

traintime=int(len(ndif)/3)
traindif=ndif[0:traintime].copy()
#df.index=range(len(df))

opdif=ndif[traintime:].copy() #Dif
opbid=nbid[traintime:].copy() #Act0 Act1 
opask=nask[traintime:].copy() #Act0 Act1 

#plt.plot(opdif)

expMult=[2]
expN=[1]

mu,sigma=traindif.mean(),traindif.std()
result=pd.DataFrame(index=[expN,'op'],columns=expMult)
operaciones=np.zeros((10,6))
Mvect = np.zeros(len(opdif))
Mvect[0]=0
spd=100000
for mult in expMult:
    for n in expN:
        C=np.array([Cinic,Cinic]) #Act0 Act1 
        M=0
        cont=0
        PosAbierta=False
        for i in range(1,len(opdif)):
            Mvect[i]=Mvect[i-1]
            if (opdif[i]-mu>mult*sigma and opdif[i-1]-mu<=mult*sigma
                and opask[i,0]-opbid[i,0]<spd and PosAbierta==False): #Act1 muy caro
                C,M=dinamica.buy(0,C,M,opask[i,0],n,i) #Compro el Act0=0 barato
                C,M=dinamica.sell(1,C,M,opbid[i,1],n,i) #Vendo el Act1=1 caro
                PosAbierta=True
            elif (opdif[i]-mu<0 and opdif[i-1]-mu>=0
                  and PosAbierta==True): 
                C,M=dinamica.sell(0,C,M,opbid[i,0],n,i) #Cierro la posic Act=0
                C,M=dinamica.buy(1,C,M,opask[i,1],n,i) #Cierro la posic Act=1
                #print(i,'Cierro Posic Long Act0',M)    
                Mvect[i]=M
                cont=cont+1 
                PosAbierta=False
            elif (opdif[i]-mu<-mult*sigma and opdif[i-1]-mu>=-mult*sigma
                  and opask[i,1]-opbid[i,1]<spd and PosAbierta==False):#Act0 muy caro
                C,M=dinamica.buy(1,C,M,opask[i,1],n,i)
                C,M=dinamica.sell(0,C,M,opbid[i,0],n,i)    
                PosAbierta=True
            elif (opdif[i]-mu>0 and opdif[i-1]-mu<=0
                  and PosAbierta==True):
                C,M=dinamica.sell(1,C,M,opbid[i,1],n,i)
                C,M=dinamica.buy(0,C,M,opask[i,0],n,i)    
                #print(i,'Cierro Posic Long Act1',M)
                Mvect[i]=M
                cont=cont+1
                PosAbierta=False

        if(C[0]>0):
            C,M=dinamica.sell(0,C,M,opbid[i,0],n,i) #Cierro la posic Act=0
            C,M=dinamica.buy(1,C,M,opask[i,1],n,i) #Cierro la posic Act=1
            #print(i,'Cierro Posic Long Act0',M)    
            Mvect[i]=M
        elif(C[0]<0):
            C,M=dinamica.sell(1,C,M,opbid[i,1],n,i)
            C,M=dinamica.buy(0,C,M,opask[i,0],n,i)    
            #print(i,'Cierro Posic Long Act1',M)   
            Mvect[i]=M              
            
        result.loc[n,mult]=M
        result.loc['op',mult]=cont

        print(mult,n,cont,M,C)     

result.to_csv('resultados.dat',sep='\t')
#np.savetxt('resultados.dat', result, delimiter='\t')
#plt.plot(Mvect)   

#print(df.corr())
#pd.rolling_corr(df[ID1], df[ID2], window=10000).plot(style='-g')
#print("COCIENTE: mean std ",df["cociente"].mean(),df["cociente"].std())
#print(len(df))
"""
fig, ax1=plt.subplots()
plt.plot(Mvect)
plt.plot(opdif,"r")
ax2=ax1.twinx()
plt.plot(opbid,"g")
plt.plot(opask,"y")
"""

#Determino el valor medio y la std en la mitad de los datos

"""
print("Dif: mean std rango min max",mu,sigma,mu-mult*sigma,mu+mult*sigma)
cantidad=int(sum(np.array(np.abs(opdif-mu))>mult*sigma))
print('cantidad',cantidad)
"""