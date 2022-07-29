#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Local variables 

def function(a,b):
    return a+b
    
obj = function(5,5)
print(obj)
    


# In[47]:


# Global variables

a = 10
b = 20
def fun(n):
    
    global a,b
    a=a+70
    b=b+10
    print(a,b)
obb=fun('hell')
print(obb)

    
    


# In[52]:


#type conversion
# eg-1
a = 4
b = 5
c=(a*b)
print(c)
print(type(c))


# In[61]:


#type conversion
#eg-2

x = 'Rest'
y = 'Please'
z = (x+y)
print(z)


# In[84]:


# __init__ function or constructor



class Elementry:
    def __init__(self,hindi,maths,sci,eng,moral):
        self.hindi = hindi
        self.maths = maths
        self.sci = sci
        self.eng = eng
        self.moral = moral
    
obj = Elementry(45,56,45,67,55)
print(obj.hindi)
print(obj.maths)
print(obj.eng)
print(obj.sci)
print(obj.moral)
        


# In[87]:


# lambda function outside the def function

add = lambda a,b:a+b
print(add(2,5))


# In[88]:


# lambda function inside the def function

def func(n):
    return lambda a:a*n
mul = func(5)
print(mul(2))


# In[92]:


# string reverse using [::-1] method

st = 'MY NAME IS HARPREET'
ob = st[::-1]
print(ob)


# In[93]:


# string reverse using palindrome fun

def ispalindrome(p):
    return p[::-1]
object = ispalindrome('palindrome')
print(object)


# In[25]:


# break statement

l = [2,4,5,-1,-2,6,7]
for i in l:
    if i<0:
        break
    else:
        print(i)


# In[22]:


#continue statement

lst = [1,2,3,4,5,6]
for i in lst:
    if i==3:
        pass
    print(i)


# In[23]:


# pass statement

ls = [45,56,34,12,4]
for i in ls:
    if i==34:
        continue
    print(i)


# In[89]:


# capitalise first letter of string

stri = 'palindrome'
cap = stri.capitalize()
print(cap)


# In[79]:


# purpose of is

up = stri.isupper()
print(up , 'palindrome is not in uppercase')

low = stri.islower()
print(low, 'palindrome is in lowercase')

al = stri.isalpha()
print(al, 'palindrome is aplhabetic word')

alnum = stri.isalnum()
print(alnum, 'palindrome is alphanumeric')



# In[82]:


# (not and in ) use in python

ls1 = [1,2,3,4,5]
ls2 = [1,2,3,9,0]

for i in ls1:  
    if i not in ls2:
        print(i)


# In[91]:


# Difference between tuple and list

list = ['1','2','3','apple','%']
print(list)
# list is mutable. its elements can be modified using methods like append, slicing, zip.



tuple = ('1','2','3','4')
print(tuple)
# tuples are immutable. i.e. its elements once declared can't be modified or change.


# In[19]:


# generate random numbers in python

import random
random.randint(1,99)
    


# In[2]:


#randomize the items of a list in place in Python


from random import shuffle 
x = [ i for i in range (10)] 
shuffle (x) 
print(x)


# In[25]:


# python iterators
tuple = ("apple","banana","cherry")
res = iter(tuple)
print(next(res))
print(next(res))
print(next(res))

print('\n')

# using iterators through loop
for x in tuple:
    print(x)
    
    
print('\n')

# using iterators in class:
class Iterator:
    def __iter__(self):
        self.g = 'guava'
        self.m = 'mango'
        return self
    def __next__(self):
        x = self.g
        y = self.m
        return x,y
myclass = Iterator()
myiter = iter(myclass)
print(next(myiter))

    


# In[34]:


#python iterables
lis = [1,2,'apples','mangoes']
print(lis)

tup = (1,2,3,4,5)
print(tup)

dic = {'red apple':'2','green apple':'3'}
print(dic)


# In[69]:


#python generators
def genfun():
    for i in range(1,9):
        if i%2==0:
            yield i
            
    print(end='\n')
    for i in range(3,9):
        if i%2!=0:
            yield i
for i in genfun():
    print(i,end=' ')
            
    


# In[98]:


# squarebracket metacharacter

import re 
st = ("emma is python developer. she also knows ML and AI")
resul = re.findall(r"[edsm]",st)
print(resul)


# In[97]:


# regular expression (?)

s = 'hhh?hhh'
import re 
re.findall(r'hhh\?hhh',s)


# In[112]:


# conditinal or ternary operators 

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
    
#eg.1
a = 2
b = 4
if a == b:
    print("True")
else:
    print("False")


# # python negative indexes and why used
# 
# st = "emma is a good learner"
# print(st[0:4])
# print('\n')
# 
# print(st[-4:-1])
# 
# 
# 

# In[121]:


# Create an empty class in python

class Employee:
    pass
    
ob1 = Employee()
ob1.name = 'jonathan'
ob1.age = '23'
ob1.office = '#2324,street line,norway'


ob2 = Employee()
ob2.name = 'Emma'
ob2.age = '24'
ob2.office = '#377,Downtown street,Noida'

print("name:"+ ob1.name)
print("age:"+ ob1.age)
print("office:"+ ob1.office)
print()


print("name:"+ ob2.name)
print("age:"+ ob2.age)
print("office:"+ ob2.office)
print()
    


# In[ ]:





# In[ ]:





# In[ ]:




