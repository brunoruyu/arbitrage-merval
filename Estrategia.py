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
#df=ReadData.ReadExcel('data_I.MERV.xlsx')
df=ReadData.ReadCsv('data_IMERV.dat',ID1,ID2,tinic,tfin)
#df=ReadData.ReadExcel('test.xlsx',ID1,ID2)
#df=ReadData.ReadCsv('test.dat',ID1,ID2)

df["dif"]=df[ID1]-df[ID2]
#df["cociente"]=df[ID1]/df[ID2]
df["NormDif"]=df["dif"]-df["dif"].mean()

mu,sigma=df["NormDif"].mean(),df["NormDif"].std()

print("NormDIF: mean std ",mu,sigma)

print(len(df[(np.abs(df['NormDif'])>3*sigma)]),len(df))


#print(df.corr())
#pd.rolling_corr(df[ID1], df[ID2], window=10000).plot(style='-g')
#print("COCIENTE: mean std ",df["cociente"].mean(),df["cociente"].std())
#print(len(df))
#fig, ax1=plt.subplots()
#df["NormDif"].plot(style="b")
#ax2=ax1.twinx()
#df["cociente"].plot(style="r")


#Determino el valor medio y la std en la mitad de los datos

