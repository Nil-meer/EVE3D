#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path
import sys


# In[2]:


variant_folder = Path("Q:\Public\B_prime_NILS\Python_files\EVE_variant_files")


# In[4]:


gene = input("Please enter the name of the gene: ")


# In[19]:


object = input("Please enter the name of the object: ")
if object=='':
    object = object
else:
    object = object + ' and '


# In[20]:


benign = input("Please enter the cut-off for benign: ")


# In[21]:


delet = input("Please enter the cut-off for deleterious: ")


# In[22]:


gene_CSV = gene + ('_HUMAN.csv')
gene_txt = gene + ('.pml')


# In[23]:


file_to_open = variant_folder / gene_CSV
txt_to_save = Path("Q:\Public\B_prime_NILS\Python_files\EVE_txt") / gene_txt
print(file_to_open)


# In[24]:


df = pd.read_csv (file_to_open)


# In[25]:


N=20
df['summe'] = df['EVE_scores_ASM'].groupby(df.index // N).sum()
df['mean'] = df['summe'].div(19)
df['mean100'] = df['mean']*100
df['mean100int'] = df['mean100'].round()
df['mean100int'] = df['mean100int'].replace(0,50)
number_residues = df.index.size//20
print(number_residues)


# In[26]:


df['b_fac'] = df['mean100int'].astype(str)
df['index1'] = df.index
df['index2'] = df['index1'].add(1)
df['aapos'] = df['index2'].astype(str)
df['b_fact'] = 'alter ' + object + 'resi ' + df['aapos'] + ', b=' + df['b_fac'] 
print (df.b_fact)


# In[30]:


with open(txt_to_save, 'w') as f:
    dfAsString = df.b_fact.head(number_residues).to_string(header=False, index=False) + '\n color white \n indicate ' + object + 'b<' + benign + '\n spectrum b, blue white, indicate, minimum=0, maximum=' + benign + '\n indicate ' + object + 'b>' + delet + '\n spectrum b, white red, indicate, minimum=' + delet + ', maximum=100'
    f.write(dfAsString)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[152]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




