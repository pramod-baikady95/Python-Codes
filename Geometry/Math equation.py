#!/usr/bin/env python
# coding: utf-8

# In[4]:


from IPython.display import display, Math

display ('4 + 3 = ' + str(4+3))


# In[6]:


x=4
y=5

display(Math(str(x) + '+' +str(y) + '=' +str(x+y)))


# In[19]:


display(Math('%g+%g = %g' %(x,y,x+y)))
display(Math('\\frac{4}{6} = 0.6666667'))


# In[20]:


x=7
y=-2
z=5

ans = 3*x*(x+y)
display(Math('3x(4+y) = %g' %ans))
display(Math("3\\times%g(4%g) = %g" %(x,y,ans)))


# In[25]:


ans = -y -(x+3)/z

display(Math('-y - \\frac{x+3}{z} = %g' %ans))
display(Math('-%g - \\frac{%g+3}{%g} = %g' %(y,x,z,ans)))

