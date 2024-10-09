#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('Hadi')


# In[4]:


x=4
y=6
x+y


# In[5]:


j=7
k=5
if j>k or k==0:
    print('Ha')


# In[9]:


h='Ayo'
a=' Hadi'
print(h+a)


# In[10]:


a=[5,6,7,8]
b=[1,2,3,4]
a[1]+b[3]


# In[11]:


ha=(5,6)
di=(4,7)
print(ha[0]+di[1])


# In[12]:


x=8
f=9
if x>f:
    print('Trap')
else:
    print('Drill')


# In[14]:


cu=0
te=4
if cu>te:
    print('Psy!')
elif cu==0:
    print('Fly Psy!')


# In[17]:


numbers=[1,2,3,4,5,6]
total=0
for num in numbers:
    total+=num
print(total)


# In[18]:


count=0
while count<=5:
    print(count)
    count+=1


# In[19]:


def greet(name):
    return"Hello! "+name
print(greet("Hadi"))


# In[20]:


person={
    "name":"Travis",
    "age":30,
    "city":"LA"
    
}
print(person)
print(person["name"])


# In[21]:


def num(h,a):
    return h+a
result=num(8,10)
print(result)


# In[22]:


import numpy as np
arr=np.zeros((6,6))
print(arr)


# In[24]:


import pandas as ps
da={'name':['Hadi','ali','mos'],
   'age':[22,22,22]}
df=ps.DataFrame(da)
print(df)


# In[2]:


for i in range(1,11):
    if i%2==0:
        print(i,"Zoj")
    else:
        print(i)


# In[3]:


#1
def check_Aval(n):
    if n>1:
        i=2
        while i*i<=n:
            if n %i==0:
                return False
            i+=1
        return True
    else:
        return False
print(check_Aval(7))


# In[13]:


#2
import numpy as ny

array1=ny.array([1,2,3,4,5])
array2=ny.array([1,2,3,4,4])

total_array1=ny.sum(array1)
total_array2=ny.sum(array2)

if total_array1>total_array2:
    print("Sum: ",total_array1," jam avali bozorg tar ast :)")
else:
    print("Sum: ",total_array2," Jam dovomi bozorg tar ast :)")


# In[15]:


#3
import numpy as ny

arra=ny.array([10,11,12,13,14,15])

def aadad_fard(array):
    for num in array:
        if num%2!=0:
            print(num)
aadad_fard(arra)
            


# In[5]:


#4
def cal(num1,num2,num3):
    sumnum=num1+num2+num3
    avg=sumnum/3
    return avg
num1=10
num2=20
num3=16

result=cal(num1,num2,num3)

if result >15:
    print("Adade ma ",result," Ast va Baalay 15 Ast")
else:
    print("Adade ma",result,"Ast Zire 15 ast")
    


# In[8]:


#5
import pandas as ps

numbers=[11,22,33,44,55,66]

dafa=ps.DataFrame(numbers,columns=['numbers'])

meanz=dafa['numbers'].mean()

print("Miangin: ",meanz)


# In[ ]:




