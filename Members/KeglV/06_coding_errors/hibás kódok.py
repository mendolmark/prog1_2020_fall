#!/usr/bin/env python
# coding: utf-8

# In[4]:


def egy():
    l1 = [5, 24, 9, 15, -4, 87]
    l2 = [6, 17, 134, -11, 26, -1]

    #A beépített len függvény egy iterálható objektum elemeinek számát adja visszatérési értékként.
    #Pl. lista elemeinek száma
    for n in range(len(l1)):

        if l1[n] > l2[n]:
            print(n)
egy()


# In[2]:


def ketto(x, y, z):
    a = float    
    if x + y > z and x + z > y and y + z > x:
        a = 'háromszög'
    
    if a == 'háromszög':
        return (x, y, z)
    else:
        return 'semmi'

ketto(1,2,3)


# In[1]:


def harom():
    k = 1
    s = 0

    while k >= 100:

        if k % 2 == 0:
            s = s + k

harom()


# In[29]:


#nem tudtam megoldani:(

def negy():
    t = [0,1,4,3]

    for i in range(len(t)):

        if (len(t) == range(t)) & (t(i) < 4):

            None
            
negy()


# In[51]:


#nem tudtam megoldani:( nem értem a ranget hogyan lehet megoldani, hogy az 5ön ne menjen túl

def ot():
    input_lista = [112,4234,721,1002,5982,1035]
    out = []
    
    
    for i in range(0,5):
    i >= 5
        
        if input_lista[i] < input_lista[i+1]:

            out[i] == input_lista[i]

        return out

ot()


# In[53]:


#nem tudtam megoldani:(

def hat():
    l = [1,1,1,1,1]

    
    while l[i] == 1:

        if l[i+1] == i:

            l[i] += 1

        else:

            'Error'
            
hat()


# In[55]:


def het():
    genya = 0
    
    for i in range(0, 10, 5):
        genya += i

    return genya
    
het()


# In[59]:


def nyolc():
    banka = "almamáter"
    tanga = ""
    for lanka in banka:
        if lanka > tanga:
            tanga = lanka
        else:
            return "kifogytam"
        
    return tanga
    
nyolc()


# In[84]:


#nem tudtam megoldani:(


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




