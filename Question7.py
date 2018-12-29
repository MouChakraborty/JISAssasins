#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Program to calculate the sum of digits of a given number By Moumita Chakraborty
num = int(input("Please Enter any Number: "))
sum = 0

while(num>0):
    rem = num % 10
    sum = sum + rem
    num = num //10

print(" Sum of the digits of Given Number ",sum)


# In[ ]:




