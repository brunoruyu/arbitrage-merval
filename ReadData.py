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

def ajustadf(df,ID0,ID1,tinic,tfin):
    df=df.dropna(axis=0)
    new0 = df[df['idSigla'] == ID0]
    new1 = df[df['idSigla'] == ID1]    
    new0=new0.drop_duplicates(subset="TimeStamp",keep="last")
    new1=new1.drop_duplicates(subset="TimeStamp",keep="last")    
    df1=pd.concat([new0,new1])
    df1["prom"]=(df1.bid+df1.offer)/2

    dff=pivotear(df1,'prom',tinic,tfin)
    dff["dif"]=dff['Act1']-dff['Act0']

    bid=pivotear(df1,'bid',tinic,tfin)
    ask=pivotear(df1,'offer',tinic,tfin)
    #df["cociente"]=df[ID1]/df[ID2]
    return (dff,bid,ask)

def pivotear(df,text,tinic,tfin):
    dff = df.pivot(index='TimeStamp', columns='idSigla', values=text)
    dff=dff.fillna(method='pad')
    dff=dff.dropna(axis=0)
    dff=dff[tinic:tfin]
    dff.columns=[['Act0','Act1']]
    return dff
    
    
def ReadExcel(archivo,ID0,ID1):
    cols=["idSigla","TimeStamp","bid","offer"]
    df=pd.read_excel(archivo,sheetname="Hoja1",index_col=None,
                     usecols=cols)
   # print(df)
    (dff,bid,ask)=ajustadf(df,ID0,ID1,tinic,tfin)
    return (dff,bid,ask)
    #print(dff)

def ReadCsv(archivo,ID0,ID1,tinic,tfin):
    cols=["idSigla","TimeStamp","bid","offer"]  
    df=pd.read_csv(archivo,index_col=None,sep="\t",usecols=cols,decimal=","
                   ,parse_dates=True)

    (dff,bid,ask)=ajustadf(df,ID0,ID1,tinic,tfin)
    return (dff,bid,ask)

