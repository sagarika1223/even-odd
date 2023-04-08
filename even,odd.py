#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9,11,12) 
num_1 = 0
num_2= 0
for x in numbers:
        if not x % 2:
         num_1+=1
        else:
         num_2+=1
print("Number of even numbers :",num_1)
print("Number of odd numbers :",num_2)


# In[ ]:




