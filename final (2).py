# -*- coding: utf-8 -*-
"""final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aXW8t1QWWolcKgu6Lu14R009g3_YB6tx
"""

import numpy as np
import pickle
import pandas as pd
import datetime
import re
from prettytable import PrettyTable
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder,normalize
from keras.models import load_model

class final:
  def final(self,page,date):
    k=date.split("-")
    date2=datetime.date(int(k[0]),int(k[1]),int(k[2]))
    data=pd.read_csv("final.csv")
    index=data[data["Page"]==page].index.values
    print(data.iloc[index[0]])
    index_column=data.columns.get_loc(str(date2))-804
    k =np.array(data.iloc[index[0]].values[-200+index_column:index_column], dtype=int) 
    x_pred=k[:200] 
    x_pred=np.log1p(x_pred)
    access=[]
    agent=[]
    language=[]
    temp=page.split(".")
    k=temp[-3].split("_")
    if k[-1]=="commons" or k[-1]=="www":
      language.append("media")
    else:
      language.append(k[-1])
    t=temp[-1].split("_")
    access.append(t[1])
    agent.append(t[2])
    with open('enc_access','rb') as file:
      access_enc=pickle.load(file) 

    with open('enc_language','rb') as file:
      lang_enc=pickle.load(file)

    with open('enc_agent','rb') as file:
      agent_enc=pickle.load(file)
    access_ohe=access_enc.transform([access]).reshape(1,1)
    agent_ohe=agent_enc.transform([agent]).reshape(1,1)
    language_ohe=lang_enc.transform([language]).reshape(1,1)
    model=load_model("lstm.h5")
    x_pred=np.array(x_pred).reshape(1,200,1)
    pred=model.predict([x_pred,access_ohe,language_ohe,agent_ohe])
    pred=np.expm1(pred)
    return agent[0],access[0],language[0],int(pred[0][0])

