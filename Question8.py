#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Program to swap the values of two variables using Call by Reference By Moumita Chakraborty
x = int(input("Enter first number"))
y = int(input("Enter second number"))
def swap(w,v):
    return v,w
x,y=swap(x , y)
print(x)
print(y)

