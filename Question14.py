#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Program to accept 'n' numbers from user and store these numbers  into an array and count the number into an array and count the number of occurences of each number
from collections import Counter
z=[]
x=int(input("Enter the number of inputs u want to give"))
for y in range(x):
    a=int(input("Enter the number"))
    z.append(a)
Counter(z)


# In[ ]:





# In[ ]:




