#!/usr/bin/env python
# coding: utf-8

# In[32]:


# added two strings of any base n (n<=16)
def add_n_base_numbers(a: str, b: str, nbase=2) -> str:
    # bin: nbase = 2
    # hexa: nbase = 16
    if nbase == 0:
        return 'Invalid base'
    if len(a) < len(b):
            a, b = b, a
    n1, n2 = len(a), len(b)
    if n1 == 0 or n2 == 0:
        return None
    get_str_representation = lambda i: str(i) if i < 10 else chr(i+55)
    str_int_dict = {get_str_representation(i): i for i in range(0, nbase)}
    int_str_dict = {i: get_str_representation(i) for i in range(0, nbase)}
    a, b = a.upper(), b.upper()
    carry = 0
    result = ''
    for i in range(1, n1+1):
        ai = a[-i]
        bi = b[-i] if i <= n2 else None
        tot = str_int_dict.get(ai, 0) + str_int_dict.get(bi, 0) + carry
        carry = tot // nbase
        result = int_str_dict.get(tot % nbase) + result
    if carry == 1:
        result = str(carry) + result
    return result
            
            


# In[33]:


add_n_base_numbers('1', '0', 0)


# In[ ]:




