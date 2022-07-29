#!/usr/bin/env python
# coding: utf-8

# In[14]:


# check whether the given number is prime or not

num = 55
flag = False
if num>1:
    for i in range(2,num):
        if num%2==0:
            flag = True
            break
if flag:
    print(num, "is not prime number")
else:
    print(num, "is prime number")


# In[18]:


# Print sum of two numbers

num1 = 23
num2 = 12
sum = num1+num2
print("The sum of {0} and {1} is {2}".format(num1,num2,sum))


# In[19]:


# swap two variables
x = 3
y = 6
x,y=y,x
print("x =",x)
print("y =",y)


# In[37]:


# generate random numbers in python
import random
random.randint(1,10)

        


# In[43]:


# check if number is positive,negative or 0

num = float(input("Enter any number: "))
if num>0:
    print("Positive number")
elif num==0:
    print("Zero")
else:
    print("Negative number")


# In[45]:


# check whether number is odd or even

no = 2
if no%2==0:
    print("2 is Even number")
else:
    print("2 is not even number")


# In[48]:


# check whether the given year is leap year or not

year = 2200
if (year%400==0) and if (year%100==0):
    print("{}is leap year".format(year))
if (year%4==0) and if (year%100!=0):
    print("{} is leap year".format(year))
else:
    print("{} is not a leap year".format(year))
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




