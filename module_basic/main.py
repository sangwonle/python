#!/usr/bin/env python
# coding: utf-8

# In[9]:


import test_module as test

print('main name : ', __name__)
radius = test.number_input()

print('{:.3f}'.format(test.get_circum(radius)))
print(test.get_circle_area(radius))

