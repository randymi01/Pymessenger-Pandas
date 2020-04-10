#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
import os

contacts = pd.read_csv("formatted_contacts.csv")
contacts = contacts[contacts.columns[contacts.shape[1]-4:contacts.shape[1]]]

# In[7]:
def remove_non_nums(num):
    numbers = [str(i) for i in range(0,10)]
    num = str(num)
    return "".join(i for i in num if i in numbers)

# 1. If val in last name or first name is nan, replace with item from other col. If both are nan, remove from data frame.
contacts.drop(contacts[np.logical_and(contacts["Last Name"].isna(), contacts["First Name"].isna()) == True].index, inplace = True)
contacts["Last Name"] = contacts["Last Name"].where(contacts["Last Name"].isna() == False).fillna(contacts["First Name"])
contacts["First Name"] = contacts["First Name"].where(contacts["First Name"].isna() == False).fillna(contacts["Last Name"])
contacts["fullname"] = contacts[contacts["First Name"] == contacts["Last Name"]]["First Name"]
contacts["fullname"] = contacts["fullname"].fillna(contacts["First Name"] + ' ' + contacts["Last Name"])
contacts["Phone Number"] = contacts["Phone Number"].apply(remove_non_nums)



contacts.to_csv("formatted_contacts.csv", encoding='utf-8')

def addcontact(name,pnum,df):
    df = df.append({'First Name' : name , 'Last Name' : name, "Phone Number" : remove_non_nums(pnum), "fullname" : name},ignore_index = True)
    df.to_csv("formatted_contacts.csv", encoding='utf-8')
    return df

#contacts = addcontact("testingman",12345678, contacts)



# In[ ]:
