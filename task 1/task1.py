#!/usr/bin/env python
# coding: utf-8

# In[122]:


# to find sum of values of key using built-in method

from collections import Counter
d1={'a': 100,'b': 200,'c': 300}
d2={'a': 200, 'b':300,'c': 400}
obj=Counter(d1)+Counter(d2)
print(obj)


# In[119]:


#to find sum of values of keys without inbuilt method

d1={'a': 100,'b': 200,'c': 300}
d2={'a': 200, 'b':300,'c': 400}
for key in d2:
    if key in d2:
        d2[key]=d2[key]+d1[key]
    
print(d2)


# In[120]:


# count numer of characters(character frequency) in a string

def count(str):
    dic={}
    for n in str:
        keys=dic.keys()
        if n in keys:
            dic[n]+=1
        else:
            dic[n]=1
    return dic
print(count('google.com'))


# In[53]:


#WAP to get single string from two given strings,separated by a 
#space and swap the first two characters of each string.(slicing concepts)
# using builtin method

def replace(st1,st2):
    stri=st1.replace(st1[0:2],st2[0:2])
    strin=st2.replace(st2[0:2],st1[0:2])
    
    return stri,strin
print(replace('abc','xyz'))
    
        


# In[75]:


#WAP to get single string from two given strings,separated by a 
#space and swap the first two characters of each string.(slicing concepts)
# without built-in method

st1,st2='abc','xyz'
ob = st1[0:2]+st2[2:]
obj = st2[0:2]+st1[2:]
print(ob,obj)

