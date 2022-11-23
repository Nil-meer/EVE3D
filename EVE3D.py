#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path
import sys
import os


# In[2]:


FOLDER_DIR = os.path.dirname(os.path.realpath('__file__'))
print (FOLDER_DIR)


# In[3]:


input_path = ("EVE_csv")
output_path = ("Output")


# In[4]:


true_input_path = os.path.join(FOLDER_DIR, input_path)
true_output_path = os.path.join(FOLDER_DIR, output_path)
print (true_output_path)


# In[5]:


gene = input("Please enter the name of the gene as depicted on EVE website: ")


# In[6]:


object = input("Please enter the PyMOL object name of your protein: ")
if object=='':
    object = object
else:
    objec = object
    object = object + ' and '


# In[7]:


benign = input("Please enter the cut-off for benign multiplied by 100: ")


# In[8]:


delet = input("Please enter the cut-off for pathogenic multiplied by 100: ")


# In[9]:


gene_CSV = gene + ('_HUMAN.csv')
gene_txt = gene + ('.pml')


# In[10]:


file_to_open = os.path.join(true_input_path, gene_CSV)
txt_to_save = os.path.join(true_output_path, gene_txt)
txt_to_save2 = os.path.join(true_output_path, gene_CSV)
print(file_to_open)


# In[11]:


try:
    df = pd.read_csv (file_to_open)
except:
    gene = input("Input datasheet does not exist in EVE_vcf folder")
    exit ()


# In[12]:


N=20
df['summe'] = df['EVE_scores_ASM'].groupby(df.index // N).sum()
df['mean'] = df['summe'].div(19)
df['mean100'] = df['mean']*100
df['mean100int'] = df['mean100'].round()
df['mean100int'] = df['mean100int'].replace(0,50)
number_residues = df.index.size//20


# In[13]:


df['b_fac'] = df['mean100int'].astype(str)
df['index1'] = df.index
df['index2'] = df['index1'].add(1)
df['aapos'] = df['index2'].astype(str)
df['b_fact'] = 'alter ' + object + 'resi ' + df['aapos'] + ', b=' + df['b_fac'] 


# In[14]:


df.to_csv(txt_to_save2)


# In[15]:


with open(txt_to_save, 'w') as f:
    dfAsString = df.b_fact.head(number_residues).to_string(header=False, index=False) + '\n color white, ' + objec + ' \n indicate ' + object + 'b<' + benign + '\n spectrum b, blue white, indicate, minimum=0, maximum=' + benign + '\n indicate ' + object + 'b>' + delet + '\n spectrum b, white red, indicate, minimum=' + delet + ', maximum=100'
    f.write(dfAsString)
