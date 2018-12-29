#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program to accept a sentence from the user and reverse its each word By Moumita Chakraborty
s=input("Enter the sentence") 
w = s.split(" ")    
nw = [i[::-1] for i in w]
ns = " ".join(nw)
print("The reverse is",ns)


# In[ ]:




