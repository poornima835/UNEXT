#!/usr/bin/env python
# coding: utf-8

# In[4]:


def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
factorial(5)


# In[6]:


#fibonacci
def fib(n):
    if n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


fib(8)


# In[10]:


def div(a,b):
    c=a/b
    return c
div(8,4)
#div(3,15)


# In[11]:


div(b=3,a=15)


# In[12]:


def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner


# In[13]:


result=smart_div(div)
result(10,5)


# In[15]:


result(5,10)


# In[19]:


def wish(name):
    print("Hello",name,", Good Morning!!")
wish("poornima")
    


# In[21]:


wish("poorni")
wish("poornima")
wish("raghuwanshi")


# Task3: Logging Decorator
# 
#  
# 
# You are tasked with creating a decorator function called log_function_call that logs when a function is called, along with its arguments, and the result of the function call. You will apply this decorator to two functions.
# 
#  
# 
# Implement a decorator function called log_function_call that takes a function as an argument and wraps it. Inside the decorator, log the function's name, its arguments, and the result of the function call. You can use the logging module for logging.
# 
#  
# 
# Create two functions:
# 
#  
# 
# add(a, b): This function takes two integers, a and b, as arguments and returns their sum.
# multiply(a, b): This function takes two integers, a and b, as arguments and returns their product.
# Apply the log_function_call decorator to both the add and multiply functions.
# 
#  
# 
# Call the decorated add and multiply functions with different arguments to verify that the decorator logs the function calls and results correctly.

# In[23]:


def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
add(10,20)
multiply(2,5)


# TASK-4: To generate fibonacci number using generator function
# 

# In[24]:


def fib_generator(n):
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
        
for i in fib_generator(6):
    print(i)


# In[3]:


nos=[1,2,3,4,5]
square=[x**2 for x in nos]
print(square)


# In[4]:


s=[x*2 for x in range(5)]
print(s)


# In[5]:


nos=[1,2,3,4,5,6,7,8]
l=[x for x in nos]
print(l)


# In[22]:


new=[i[0].upper() for i in lst]
print(new)


# In[7]:


lst=["python","c++","c","js"]
l=[i[0] for i in lst]
print(l)


# In[9]:


#counting words and splitting them
words="be in your bonnet, Potter!!"
op=[[i.upper(),len(i)] for i in words.split()]
print(op)


# LAMBDA FUNCTION/ ANONYMOUS FUNCTION
# #function without name 
# #use keyword lambda

# In[13]:


f=lambda i:i*i
f(5)


# In[18]:


##lambda function to add
add=lambda a,b:a+b
print(add(4,5))


# In[19]:


##largest between 2 numbers using lambda function 
largest=lambda a,b:a if a>b else b
largest(3,4)


# In[26]:


#filter, map, reduce

l=[0,2,3,4,5,6,8]
l1=list(filter(lambda x:x%2==0,l))
print(l1)


# # CLASS
# --acts as a blueprint
# --class consists of attributes/methods/functions and variables
# --

# In[28]:


class computer:
    #variables
    #methods/attributes
    def config(self):
        print("i5", "16GB")


# In[32]:


#object of classs
comp=computer()


# In[33]:


comp.config()


# In[ ]:




