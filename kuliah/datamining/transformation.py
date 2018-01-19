from __future__ import division
import pandas as pd
import numpy as np

def minmax(data,newmin=0,newmax=1):
    newdata = []
    for i in range(0,len(data.columns)):
        minval = min(data[i])
        maxval = max(data[i])

        t = []
        for val in data[i]:
            c = (val-minval)*(newmax-newmin)/(maxval-minval)+newmin
            t.append(c)
        newdata.append(t)
    return pd.DataFrame(newdata).transpose()

def zscore(data):
    newdata = []
    for i in range(0,len(data.columns)):
        mean = np.mean(data[i])
        std = np.std(data[i], ddof=1)
        print mean
        t = []
        for val in data[i]:
            c = (val-mean)/std
            t.append(c)
        newdata.append(t)
    return pd.DataFrame(newdata).transpose()

def decimal(data,i=1):
    newdata = []
    for i in range(0,len(data.columns)):
        t = []
        for val in data[i]:
            c = val/10**i
            t.append(c)
        newdata.append(t)
    return pd.DataFrame(newdata).transpose()

def sigmoid(data):
    newdata = []
    for i in range(0,len(data.columns)):
        mean = np.mean(data[i])
        std = np.std(data[i], ddof=1)
        t = []
        for val in data[i]:
            x = (val-mean)/std
            c = (1-np.exp(-1*x))/(1+np.exp(-1*x))
            t.append(c)
        newdata.append(t)
    return pd.DataFrame(newdata).transpose()

def softmax(data,x=1):
    newdata = []
    for i in range(0,len(data.columns)):
        mean = np.mean(data[i])
        std = np.std(data[i], ddof=1)
        t = []
        for val in data[i]:
            transfdata = (val-mean)/(x*(std/(2*3.14)))
            c = 1/(1+np.exp(-1*transfdata))
            t.append(c)
        newdata.append(t)
    return pd.DataFrame(newdata).transpose()
