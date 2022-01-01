#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("Twinkle,Twinkle,little star")
print("       How i wonder What you are!")
print("              up above the world so high,")
print("              like a diamand in the sky")
print("Twinkle,Twinkle,little star")
print("       How i wonder What you are")


# In[7]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[8]:


import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))


# In[9]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# In[11]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)


# In[12]:


x = input("Type a number: ")
y = input("Type another number: ")

sum = int(x) + int(y)

print("The sum is: ", sum)


# In[ ]:




