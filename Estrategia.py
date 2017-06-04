# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:47:46 2017

@author: bruno
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import ReadData

ID1,ID2=39,69   
tinic,tfin="2016-10-03 12:09:46","2016-12-29 17:05:51"
Cinic=100
mult=3

(df,bid,ask)=ReadData.ReadCsv('data_IMERV.dat',ID1,ID2,tinic,tfin)
#df=ReadData.ReadExcel('data_I.MERV.xlsx')
#df=ReadData.ReadExcel('test.xlsx',ID1,ID2)
#df=ReadData.ReadCsv('test.dat',ID1,ID2)

limit=int(len(df)/3)
traindf=df[0:limit].copy()
opdf=df[limit:].copy()
opbid=bid[limit:].copy()
opask=ask[limit:].copy()

print(opdf)
mu,sigma=traindf["dif"].mean(),traindf["dif"].std()
print("Dif: mean std rango max",mu,sigma,mu+mult*sigma)

#traindf["NormDif"]=traindf["dif"]-mu #para estudiar las props

print('fuera de rango',
      len(opdf[(np.abs(opdf["dif"]-mu)>mult*sigma)]),len(opdf))

C=np.array([Cinic,Cinic])
M=np.array([opdf.iat[0,0]*Cinic,opdf.iat[0,1]*Cinic])
#M=np.array([opdf.at[tfin,ID1],opdf[tfin,ID2])

cont=0
i=0
for row in opdf.itertuples():
    i=i+1
    if row[3]-mu>mult*sigma:
        
        cont=cont+1
#        print(i,cont)
print(cont)


   
#print(df.corr())
#pd.rolling_corr(df[ID1], df[ID2], window=10000).plot(style='-g')
#print("COCIENTE: mean std ",df["cociente"].mean(),df["cociente"].std())
#print(len(df))
#fig, ax1=plt.subplots()
#df["NormDif"].plot(style="b")
#ax2=ax1.twinx()
opdf["dif"].plot(style="r")


#Determino el valor medio y la std en la mitad de los datos

