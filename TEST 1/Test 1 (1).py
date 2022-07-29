#!/usr/bin/env python
# coding: utf-8

# In[1]:


# WAP to replace vowel by * from given number
def replace(check, k):
    vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    l = []
    stlist = check
    for char in stlist:
        for char2 in vowel:
            if char==char2:
                l.append(k)
                break
        else:
            l.append(char)
            
    return(''.join(l))
check = 'visiontrekcommunications'
k = '*'
print('Initial string :- ',check)
print('Replace initial string vowel with :- ',k)
print('Replaced string is :- ',replace(check,k))
                
                


# In[108]:


# add two list into dictionary
key_list = ["key","key1","key3"]
value_list = ["1","abc","3"]    
def list_to_dic(key_list,value_list):
    new_dic = {}
    if len(key_list) != 0 and len(value_list) != 0:
        for i in range(len(key_list)):
            new_dic[key_list[i]] = value_list[i]
    return new_dic
print(list_to_dic(key_list,value_list))


# In[4]:


# reverse a string

strr = "123chjcbsjhbjhsd"
print("Initial string is :-",strr)
new = " "
for i in strr:
    print(i)
    new=i+new
print("reversed string is :- ",new)




# In[51]:


# two max and two min number print

list = [2,22,56,78,89,90,43,1]
l1=[]
l2=[]
data = data+1
max = 0
for data in list:
        if data > max:
            max = data
            l1.append(data)
        
        
print('The first large number is:-', max)




# In[20]:


# WAP to print an output

list = ["String","vision","communications"]
ll = []
for word in list:
    for char in word:
        ll.append(char)
        
print(ll)
        
        


# In[193]:


# print odd and even in string

liss = ["abc","xyzs","cdzf"]

even_st  = []
odd_st = []

for i in liss: 
    if len(i) %2 == 0: 
        even_st.append(i)
        print(i,': Even')
    else: 
        odd_st.append(i) 
        print(i,': Odd')


# In[6]:


# print first two largest and smallest number from list
 
def find_smallest_largest(arr):
    secondLargest = arr[0]
    largest = arr[0]
    smallest = arr[0]
    secondSmallest = arr[0]

    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(len(arr)):
        if arr[i] > secondLargest and arr[i] != largest:
            secondLargest = arr[i]
            
            
    
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            
    for i in range(len(arr)):
        if arr[i] < secondSmallest and arr[i] != smallest:
            secondSmallest = arr[i]
            
    return secondLargest,largest,smallest,secondSmallest

print("First two largest and smallest elements are :- ")
print(find_smallest_largest([10,35,85,27,-1]))


# In[ ]:


# WAP if user enter a number

numb = int(input("Enter any number :- "))
add_num = 0 

for i in range(0,numb):
    for j in range(i,numb):
        numb+=add_num
        add_num+=10
        print(numb)
        
    
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




