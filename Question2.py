#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program to accept 'n' numbers from user, store these numbers into an array and find the max and min number from it By Moumita Chakraborty
num=[]
n=int(input("How many numbers u want to enter"))
for i in range(1,n+1,1):
    x=int(input("Enter the number "))
    num.append(x)
print("The numbers in the array are",num)
print("Max number in array is",max(num))
print("Min number in array is",min(num))


# In[ ]:




