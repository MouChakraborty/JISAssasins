#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a menu driven program to perform following:-
#-Calculate length of string
#-Reverse a given string
#-Concatenation of string to another
#-Copy  one string into another
#-Compare two strings By Moumita Chakraborty
X = input("Enter your string")
l=len(X)
print("The length is", l)
Y = "Moumita"
Z= X+Y
print("After concatenation", Z)
print(''.join(reversed(X)))
old="I like Python"
new=old.replace("like","love")
print(new)
if X == Y:
    print("Equal")
else:
    print("Not Equal")


# In[ ]:




