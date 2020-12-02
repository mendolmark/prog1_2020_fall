#!/usr/bin/env python
# coding: utf-8

# In[1]:


def egy():
    l1 = [5, 24, 9, 15, 34, 87]
    l2 = [6, 17, 134, -11, 26, -1]

    #A beépített len függvény egy iterálható objektum elemeinek számát adja visszatérési értékként.
    #Pl. lista elemeinek száma
    for n in range(len(l1)):

        if l1[n] > l2[n]:
            print(n)
egy()


# In[2]:


def ketto(x, y, z):
    
    if x + y > z and x + z > y and y + z > x:
        a = 'háromszög'
    
    else:
        return 'semmi'

ketto(1,2,3)


# In[13]:


def ketto(x, y, z):
    
    x = 3
    y = 5
    z = 7
       
    if x + y > z and x + z > y and y + z > x:
        a = 'háromszög'
    
    if a == 'háromszög':
        return (x, y, z)
    else:
        return 'semmi'

ketto(1,2,3)


# In[14]:


def harom():
    k = 1
    s = 0

    while k <= 100:
        if k % 2 == 0:
            s = s + k
        k += 1

harom()


# In[15]:


def negy():
    t = [0,1,4,3]

    for i in range(len(t)):

        if (len('alma') == range(i)) & (t[i] < 4):

            None
            
negy()


# In[20]:


def ot():
    input_lista = [112,4234,721,1002,5982,1035]
    out = ["tibi"]

    for i in range(0,10):

        if input_lista[i] > input_lista[i+1]:
            
            out == input_lista[i]

        return out    
ot()


# In[22]:


def hat():
#nemmegy
    l = [1,1,1,1,1]
    I = 1

    while l[i] == 1:

        if l[i+1] == i:

            l[i] += 1

        else:

            'Error'
hat()


# In[27]:


def het():
    genya = 0
    
    for i in range(0, 10):
        genya += i

    return genya
    
het()


# In[42]:


def nyolc():
    banka = "almamáter"
    tanga = "x"
    for lanka in banka:
        if lanka > tanga:
            tanga = lanka
        else:
            return banka
        
    return tanga
nyolc()


# In[ ]:


#ez már sok
def kilenc():
        árán = ""
        száján = "szárán"
    while len(árán) < 5:
    árván = száján * 2
        kárán = len(száján) // 3
        
            for bárány in száján:
            if száján[kárán] == bárány:
                álcám = True
                else:
                álcám = False
        
        if álcám:
            lányán = False
                fácán = True
        else:
            lányán = True
            fácán = False
        
if lányán:
    árán += "m"
elif fácán:
    árán += "n"
else:
    hamutálcán = "pusztulásán"
            
    return árán
kilenc()

