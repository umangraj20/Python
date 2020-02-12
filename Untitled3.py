#!/usr/bin/env python
# coding: utf-8

# In[5]:


l1=[1,3,5,43,21,22,24]
l2=[2,4,5,34,65,76,12]
l3=[]
for i in range (0,len(l1)):
    if l1[i]%3==0:
        l3.append(l1[i])
for i in range (0,len(l2)):
    if l2[i]%3==0:
        l3.append(l2[i])
print (l3)        


# In[6]:


l1=[1,3,5,43,21,22,24]
l2=[2,4,5,34,65,76,12]
l3=[]
for i in range (0,len(l1)):
    if l1[i]%3==0 or l1[i]%4==0:
        l3.append(l1[i])
for i in range (0,len(l2)):
    if l2[i]%3==0 or l2[i]%4==0:
        l3.append(l2[i])
print (l3)        


# In[8]:


t1=(1,2,3,4)
l1=list(t1)
for i in range (0,len(l1)):
    print (l1[i])


# In[ ]:




