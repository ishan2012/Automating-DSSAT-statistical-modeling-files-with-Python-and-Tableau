
# coding: utf-8

# In[73]:


import os


# In[74]:


os.getcwd()


# In[75]:


os.chdir('C:\\Users\\Ishan Malpotra\\Desktop\\Internship')


# In[76]:


os.getcwd()


# In[77]:


import pandas as pd


# In[78]:


import numpy as np


# In[79]:


import matplotlib.pyplot as plt


# In[80]:


import re


# In[81]:


sample_data = open('PlantGro.txt')


# In[82]:


line=sample_data.readline()


# In[83]:


if line.startswith('$') or line.startswith('*'):
    filename=str(line)


# In[84]:


filename


# In[85]:


filename = re.sub('[*$\n]', '', filename)


# In[101]:


filename


# In[102]:


s = open("PlantGro.txt").read()


# In[103]:


count=1
while count==1:
    count=0
    count1=0
    for i in s:
        if i=='*':
            count1+=1
        if i=='@':
            count+=1
        if count1==1:
            x=s.index('*')
        if count==1:
            y=s.index('@')+1
            s=s[:x]+s[y:]
            break


# In[104]:


s


# In[105]:


s=re.sub("[$].*[\n]", "", s)


# In[106]:


list = (re.split("[\n]",s))


# In[107]:


while '' in list:
    list.remove('')


# In[108]:


list


# In[109]:


len(list)


# In[110]:


import string


# In[111]:


letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in list:
    if i[0] in letters:
        indexes = [index for index in range(len(list)) if list[index] == i]


# In[112]:


indexes


# In[113]:


def partition(list, indexes):
    return [list[i:j] for i, j in zip([0]+indexes, indexes+[None])]


# In[114]:


dataframe=partition(list,indexes)


# In[115]:


del dataframe[0]


# In[116]:


len(dataframe)


# In[117]:


from pandas import ExcelWriter


# In[118]:


def save_xls(list_dfs, xls_path):
    writer = ExcelWriter(xls_path)
    for n, df in enumerate(list_dfs):
        pd.DataFrame(df).to_excel(writer,'run%s' % (n+1),index=False,header=False)
    writer.save()


# In[121]:


save_xls(dataframe,'C:\\Users\\Ishan Malpotra\\Desktop\\Internship\\%s.xls' % filename)

