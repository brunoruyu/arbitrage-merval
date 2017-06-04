# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 19:55:06 2017

@author: bruno
"""
import numpy as np
import pandas as pd

fixc=3.0 #0.19*16.5
prop=0.001

def buy(Act,C,M,price,n):
    C[Act]=C[Act]+n
    cost=fixc+prop*price*n
    M=M-n*price-cost    
    return (C,M)
    
def sell(Act,C,M,price,n):
    C[Act]=C[Act]-n
    cost=fixc+prop*price*n
    M=M+n*price-cost    
    return (C,M)   