#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Program to add information of book and display it By Moumita Chakraborty
class Book:
    def id1(self):
        self.id_num=int(input("Please enter id\n"))
    def cost(self):
        self.book_cost=int(input("Please enter cost\n"))
    def author(self):        
        self.auth_name=input("Please enter author\n")
    def bookdb(self):
             print("BOOK ID: {} BOOK COST:{} BOOK AUTHOR:{} ".format(self.id_num,self.book_cost,self.auth_name))
b=Book()
b.id1()
b.cost()
b.author()
b.bookdb()


# In[ ]:




