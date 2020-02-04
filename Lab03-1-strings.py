#!/usr/bin/env python
# coding: utf-8

# In[1]:


#exercise 2


# In[2]:


word = "banana"


# In[3]:


word.count("a")


# In[5]:


#exercise 3


# In[28]:


a = " acvtjme"


# In[9]:


def middle(n):
    return n[1: -1]


# In[29]:


middle(a)


# In[31]:


def first(word):
    return word[0]


# In[32]:


def last(word):
    return word[-1]


# In[40]:


def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))
#Returns True if word is a palindrome.


# In[41]:


is_palindrome("omlpmo")


# In[42]:


#exercise 4


# In[43]:


def is_power(a,b):
    if a%b == 0 and (a/b)%b == 0:
        return True
    


# In[ ]:


#exercise 5


# In[44]:


def gcd(a,b):
    if a%b == 0:
        return b
    if b%(a%b) == 0:
        return a%b
    return 1


# In[45]:


gcd(5,3)


# In[47]:


gcd(3,6)


# In[48]:


gcd(15,6)


# In[ ]:




