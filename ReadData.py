# -*- coding: utf-8 -*-
"""
Created on Thu May 18 18:48:35 2017

@author: bruno
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:56:34 2017

@author: bruno
"""
import numpy as np
import pandas as pd
    

#file_handle = open('datos_test.dat', 'r')
# Read in all the lines of your file into a list of lines
#lines_list = file_handle.readlines()
#read = [[float(val) for val in line.split()] for line in lines_list[0:]]
#df=pd.DataFrame(read,columns=["inst","time","bid","ask"])

def ajustadf(df,ID1,ID2):
    df1=df.dropna(axis=0)
    new1 = df1[df1['idSigla'] == ID1]
    new2 = df1[df1['idSigla'] == ID2]    
    new1=new1.drop_duplicates(subset="TimeStamp",keep="last")
    new2=new2.drop_duplicates(subset="TimeStamp",keep="last")    
    df1=pd.concat([new1,new2])
    df1["prom"]=(df1.bid+df1.offer)/2
    dfp = df1.pivot(index='TimeStamp', columns='idSigla', values='prom')
    dff=dfp.fillna(method='pad')
    dff=dff.dropna(axis=0)
#    print(dff)
    return dff

def ReadExcel(archivo,ID1,ID2):
    cols=["idSigla","TimeStamp","bid","offer"]
    df=pd.read_excel(archivo,sheetname="Hoja1",index_col=None,
                     usecols=cols)
   # print(df)
    dff=ajustadf(df,ID1,ID2)
    return dff
    #print(dff)

def ReadCsv(archivo,ID1,ID2):
    cols=["idSigla","TimeStamp","bid","offer"]  
    df=pd.read_csv(archivo,index_col=None,sep="\t",usecols=cols,decimal=","
                   ,parse_dates=True)

    dff=ajustadf(df,ID1,ID2)
    return dff

