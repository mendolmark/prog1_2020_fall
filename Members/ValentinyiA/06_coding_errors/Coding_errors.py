#!/usr/bin/env python
# coding: utf-8

# In[4]:


def egy():
    l1 = [3, 5, 24, 9, 15, -4]
    l2 = [6, 17, 134, -11, 26, -1]
    
    #A beépített len függvény egy iterálható objektum elemeinek számát adja visszatérési értékként.
    #Pl. lista elemeinek száma
    for n in range(len(l1)):
        
        if l1[n] > l2[n]:
            print(n)
egy()


# In[8]:


def ketto(x, y, z):
    a = ''
    if x + y > z and x + z > y and y + z > x:
         a = 'háromszög'
            
    if a == 'háromszög':
        return (x, y, z)
    else:
        return 'semmi'

ketto(1,2,3)


# In[11]:


def harom():
    k = 1
    s = 0

    while k <= 100:

        if k % 2 == 0:
            s = s + k
        k = k + 1

harom()


# In[15]:


def negy():
    t = [0,1,4,3]

    for i in range(len(t)):

        if (len('alma') == range(4)) & (t[i] < 4):

            None
            
negy()


# In[23]:


def ot():
    input_lista = [112,4234,721,1002,5982,1035]
    out = []

    for i in range(5):

        if input_lista[i] < input_lista[i+1]:

            out.append (input_lista [i])

        return out

ot()


# In[29]:


def hat():
    l = [1,1,1,1,1]
    i = 0

    while l[i] == 1:

        if l[i+1] == l[i]:

            l[i] += 1

        else:

            'Error'
            
hat()


# In[31]:


def het():
    genya = 0
    
    for i in range(0, 10, 1):
        genya += i

    return genya
    
het()


# In[35]:


def nyolc():
    banka = "almamáter"
    tanga = ""
    kifogytam = 0
    
    for lanka in banka:
        if lanka > tanga:
            tanga = lanka
        else:
            return kifogytam
        
    return tanga
    
nyolc()


# In[36]:


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


# In[ ]:




