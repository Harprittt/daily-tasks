#!/usr/bin/env python
# coding: utf-8

# In[1]:


# a.find the common letter of the word, without using inbuilt method
	
# a=['flowing','flow','flame']
# without built-in method


string1 = 'flowing'
string2 = 'flew'
for i in string1:
    if i in string2:
        print(i)


# In[2]:


#sum = 9

# # 	task : find all possible pairs which have sum equal to sum(9)
# # 	example :
# # 		3 + 6 = 9
# # 		4 + 5 = 9
	
# # 	note :	
# # 		no repeat of pairs
# # 		e.g :  4 + 5 = 9
# # 			   and 
# # 		       5 + 4 = 9
		       
# # 	both pairs have same elements hence the pair should come only once in output
# list_a = [3, 4, 5, 6, 1, 2, 7, 9, 8]

li = [3,4,5,6,1,2,7,9,8]
n=9
for i in range(len(li)-1):
    for j in range(i+1,len(li)):
        a = li[i]
        b = li[j]
        if a+b==n:
            print(f"({a}+{b})={n}")
    


# In[3]:


# # print list of duplicate character in string and print character that has maximum number of occurence in string
# # 	take input as string = "genrosysweeklytasks"
#without built-in method

s = 'genrosysweeklytasks'
common={}
for char in s:
    if char in common:
        common[char]+=1
    else:
        common[char]=1
for key,value in common.items():
    if value>1:
        print(key,end=' ')
print()

for key,value in common.items():
    if value>=4:       
        print(key,'has the maximum repeated value')
        
print()
    

