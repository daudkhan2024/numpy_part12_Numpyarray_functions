#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Shuffle


# In[10]:


import numpy as np


# In[11]:


var = np.array([1,2,3,4,5])
np.random.shuffle(var)
print(var)


# In[12]:


#Unique


# In[13]:


var1 = np.array([1,2,2,3,4,5,66,66,7,8])
x = np.unique(var1)
print(x)


# In[14]:


#gtting index number


# In[15]:


var1 = np.array([1,2,2,3,4,5,66,66,7,8])
x = np.unique(var1,return_index=True)
print(x)


# In[18]:


#counting
var1 = np.array([1,2,2,3,4,5,66,66,7,8])
x = np.unique(var1,return_index=True,return_counts=True)
print(x)


# In[23]:


#Resize
var2 = np.array([1,2,3,4,5,6,7,8])
y = np.resize(var2,(2,4))
print(y)


# In[25]:


# Flatten
var2 = np.array([1,2,3,4,5,6,7,8])
y = np.resize(var2,(2,4))
print(y)

print(y.flatten())


# In[36]:


#changing order
var2 = np.array([1,2,3,4,5,6,7,8])
y = np.resize(var2,(2,4))
print(y)

print("Flatten:",y.flatten(order = "F"))
print("Ravel :",np.ravel(y,order = "F"))
print("Ravel :",np.ravel(y,order =  "A"))
print("Ravel :",np.ravel(y,order = "K"))


# In[ ]:




