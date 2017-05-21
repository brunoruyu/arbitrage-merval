# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:47:46 2017

@author: bruno
"""
import numpy as np

import ReadData

ID1,ID2=39,69   

#df=ReadData.ReadExcel('data_I.MERV.xlsx')
df=ReadData.ReadCsv('data_IMERV.dat',ID1,ID2)
#df=ReadData.ReadExcel('test.xlsx',ID1,ID2)
#df=ReadData.ReadCsv('test.dat',ID1,ID2)

df["dif"]=df[ID1]-df[ID2]
print(df.tail)
print("mean ",df["dif"].mean())
print("Std ",df["dif"].std())
#Determino el valor medio y la std en la mitad de los datos

