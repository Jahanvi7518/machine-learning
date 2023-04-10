#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


data = pd.read_csv("C:/Users/Rekha Tomar/Desktop/DATA.csv")
print(data,"n")


# In[5]:


d = np.array(data)[:,:-1]
print("n the attributes are:",d)


# In[6]:


target = np.array(data)[:,-1]
print("n the target is:",target)


# In[8]:


def train(c,t):
    for i,val in enumerate(t):
        if val == "yes":
            specific_hypothesis =c[i].copy()
            break
            
    for i, val in enumerate(c):
        if t[i] == "yes":
            for x in range(len(specific_hypothesis)):
                if val[x] != specific_hypothesis[x]:
                    specific_hypothesis[x] = '?'
                else:
                    pass
    return specific_hypothesis
print("N THE FINAL HYPOTHESIS IS:",train(d,target))


# In[ ]:




