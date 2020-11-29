#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#egy string-et fogad paraméternek
#az összes '+' jelet ','-re, az összes '-' jelent pedig '#'-re cseréli
#és ez a módosított string a visszatérési értéke


# In[58]:


input_string = ['ide írjátok az első csapattól kapott string-et', '-', '+']


# In[59]:


#def own_func(para):
    
para = input_string

#resname = [name.replace('DA', 'ADE').replace('DC', 'CYT').replace('DG', 'GUA').replace('DT', 'THY') for name in ncp.resname()]

para = [item.replace('+', ',').replace('-', '#') for item in para]

print(para)


# In[60]:


#ellenőrzés
from func import check_rep
check_rep(own_func, p)


# In[ ]:





# In[ ]:




