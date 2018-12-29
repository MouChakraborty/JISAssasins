#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a program to accept abasic salary from user.if basic salary >=5000 then hra=15% and da=150% of basic salary.if  basic salary <5000 then hra=10% and da=110% of basic salary.Display the gross salary.By Moumita Chakraborty

bs = int(input("enter basic salary.\n"))
if bs >= 5000:
    hr = (15/100)*bs
    da = (150/100)*bs

else:
    hr = (10/100)*bs
    da = (110/100)*bs

g = bs+hr+da

print("basic salary",bs,"hra is",hr,"da is",da,"gross salary is",g)


# In[ ]:




