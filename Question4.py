#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program to accept 'n' numbers from user store these numbers into an array and sort the numbers of the array By Moumita Chakraborty
num = int(input("How many figures : ")) 
storage = []
result = []
for i in range(1,num+1):
   a = int(input("Enter value" + str(i) + " : "))
   storage.append(a)
for m in range(len(storage)):
   b = min(storage)
   storage.remove(b)
   result.append(b)
j = ' '.join(str(i) for i in result)
print(j)


# In[ ]:




