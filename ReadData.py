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

def ReadExcel(archivo):
    cols=["idSigla","TimeStamp","bid","offer"]
    
    df=pd.read_excel(archivo,sheetname="Hoja1",index_col=None,
                     usecols=cols)
    df=df.dropna(axis=0)
    df["prom"]=(df.bid+df.offer)/2
    dfp = df.pivot(index='TimeStamp', columns='idSigla', values='prom')
    dff=dfp.fillna(method='pad')
    dff=dff.dropna(axis=0)
    return dff
    #print(dff)



