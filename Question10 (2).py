#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program to accept a string from user and delete all vowels from the string and display the result By Moumita Chakraborty

string = input("Enter any string ")
newstr = string
vowels = ('a', 'e', 'i', 'o', 'u')
for x in string.lower():
    if x in vowels:
        newstr = newstr.replace(x,"")
print("New string after successfully removed all the vowels:",newstr)


# In[ ]:




