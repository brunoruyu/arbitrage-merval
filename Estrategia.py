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

ID0,ID1=39,69   
tinic,tfin="2016-10-03 12:09:46","2016-12-29 17:05:51"
Cinic=0
mult=4

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

opdif=ndif[traintime:].copy() #Ac0 Act1 Dif
opbid=nbid[traintime:].copy() #Act0 Act1 
opask=nask[traintime:].copy() #Act0 Act1 

#plt.plot(opdif)
mu,sigma=traindif.mean(),traindif.std()

"""
print("Dif: mean std rango min max",mu,sigma,mu-mult*sigma,mu+mult*sigma)
cantidad=int(sum(np.array(np.abs(opdif-mu))>mult*sigma))
print('cantidad',cantidad)
""""


C=np.array([Cinic,Cinic]) #Act0 Act1 
M=0
PosAbierta=False
cont=0
n=2
for i in range(1,len(opdif)):
    
    if (opdif[i]-mu>mult*sigma and opdif[i-1]-mu<=mult*sigma): #Act1 muy caro
        #n=1
        C,M=dinamica.buy(0,C,M,opask[i,0],n) #Compro el Act0=0 barato
        C,M=dinamica.sell(1,C,M,opbid[i,1],n) #Vendo el Act1=1 caro
        PosAbierta=True
        cont=cont+1
    elif (opdif[i]-mu<mult*sigma and opdif[i-1]-mu>=mult*sigma): 
        #n=1
        C,M=dinamica.sell(0,C,M,opask[i,0],n) #Cierro la posic Act=0
        C,M=dinamica.buy(1,C,M,opbid[i,1],n) #Cierro la posic Act=1
        PosAbierta=False
        cont=cont+1    
    elif (opdif[i]-mu<-mult*sigma and opdif[i-1]-mu>=-mult*sigma):#Act0 muy caro
        #n=1
        C,M=dinamica.buy(1,C,M,opask[i,1],n)
        C,M=dinamica.sell(0,C,M,opbid[i,0],n)    
        PosAbierta=True
        cont=cont+1
    elif (opdif[i]-mu>-mult*sigma and opdif[i-1]-mu<=-mult*sigma):
        #n=1
        C,M=dinamica.sell(1,C,M,opask[i,1],n)
        C,M=dinamica.buy(0,C,M,opbid[i,0],n)    
        PosAbierta=False
        cont=cont+1
    else:
        PosAbierta=False
#    print(i,PosAbierta)        


if(C[0]>0):
    C,M=dinamica.sell(0,C,M,opask[i,0],n) #Cierro la posic Act=0
    C,M=dinamica.buy(1,C,M,opbid[i,1],n) #Cierro la posic Act=1
elif(C[0]<0):
    C,M=dinamica.sell(1,C,M,opask[i,1],n)
    C,M=dinamica.buy(0,C,M,opbid[i,0],n)    
                   
print(mult,n,cont,M,C)     

        #print(i,opdf.index[i],cont)


   
#print(df.corr())
#pd.rolling_corr(df[ID1], df[ID2], window=10000).plot(style='-g')
#print("COCIENTE: mean std ",df["cociente"].mean(),df["cociente"].std())
#print(len(df))
#fig, ax1=plt.subplots()
#df["NormDif"].plot(style="b")
#ax2=ax1.twinx()
#opdf["dif"].plot(style="r")


#Determino el valor medio y la std en la mitad de los datos

