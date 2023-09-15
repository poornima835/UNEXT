#!/usr/bin/env python
# coding: utf-8

# In[2]:


p="python"
print(p)


# In[3]:


type(8)


# In[6]:


b="python"


# In[7]:


type(b)


# In[8]:


b='''poornima'''


# In[9]:


type(b)


# In[10]:


print(b)


# In[11]:


t='''dhfgf
hfgfgfh'''
type(t)


# In[12]:


boole=True


# In[13]:


type(boole)


# In[15]:


boolea=False
type(False)


# In[17]:


print(type(True+True))


# In[18]:


##decalare a complex number
a=2+3j
print(type(a))


# In[19]:


a=20
print(id(a))


# In[21]:


b=20
print(id(b))


# In[22]:


a=30
print(id(a))


# In[23]:


a=20
print(id(a))


# In[24]:


s="Data Engineering"
s[-2]


# In[25]:


s[2]


# In[27]:


s[5]


# In[33]:


s="abcdefghijklmnopqrstuvwxyz"
s[12:15]


# In[34]:


s[-3:-1]


# In[36]:


s[0:26]


# In[38]:


s[0:-1]


# In[39]:


a=10
b=20
print(a+b)


# In[42]:


a=3
b=2.0
print(a/b)
print(a//b)


# In[43]:


a=3
b=2
print(a/b)
print(a//b)


# In[44]:


a=10.0
b=2.0
print(a/b)
print(a//b)


# In[45]:


print(a%b)


# In[46]:


print(a**b)


# In[47]:


a=20
b=10
print(a>b)


# In[50]:


##relation operaor and or
a=True
b=False
print(a and b)
print(a or b)


# In[51]:


is_geological_survey_complete = True

is_environmental_clearance_received = True

is_market_demand_high = False



# In[52]:


should_start_drilling = is_geological_survey_complete and is_environmental_clearance_received and is_market_demand_high


# In[54]:


print("should_start_drilling?",should_start_drilling)


# In[55]:


# Boolean Variables
HasExplorationPermit = True
HasDrillingRights = True
HasEnvironmentalApproval = False
HasOilDiscovery = True


# # Logical Operations

# In[56]:


IsExplorationAllowed = HasExplorationPermit and HasDrillingRights and not HasEnvironmentalApproval
IsDiscoveryProfitable = HasOilDiscovery and (HasExplorationPermit or HasDrillingRights)


# In[57]:


print(IsExplorationAllowed)
print(IsDiscoveryProfitable)


# In[60]:


print('one'+'two')


# In[61]:


"ten"*10


# In[64]:


'ten'*10


# In[67]:


"ten"+'10'


# ## list
# Lists encl;osed in square brackets
# hetrogeneous objects are allowed
# duplicates are allowed 
# order is preserved
# indexing and slicing are possible
# Mutable in nature
# 

# In[69]:


a=[1,'poornima','abc',2,'sanju',2,'seju', True]
print(a)
print(type(a))


# In[70]:


print(type(a[0]))


# In[73]:


id(a)
#print(id(a[-1]))


# In[74]:


a.append(999)


# In[75]:


print(a)


# In[78]:


id(a)


# # Tuple
# 1. ()
# 3. Tuple is exactly same as list but,
# 2. Tuple is immutable
# 4. tuple is faster than list, because they are immutable

# In[79]:


a=("well A","2023-09-15",'Pipeline',True, 150,150)
type(a)


# In[80]:


print(a)
#order is preserved


# In[ ]:


a[3]


# In[84]:


a[2]


# In[87]:


#'tuple' object has no attribute 'append'
##a.append(88)


# # String formatter 

# In[ ]:





# # SET
# 
# 1. sets are mutable
# 

# # Dictionary 
# 1. Always access in key value pairs
# 2. Dictionaries are used to store data values in key:value pairs
# 3. Dictonary can not have duplicate keys i.e Dictionaries cannot have two items with the same key
# 4. Dictonaries are mutable
# 5. 

# # Membership operator
# 

# In[ ]:





# In[88]:


# List of Equipment
refineryEquipment = ["Crude Distillation Unit", "Catalytic Cracking Unit", "Hydrotreating Unit", "FCC Unit"]

 

# Membership Operator
IsUnitInstalled = "Hydrotreating Unit" in refineryEquipment
IsUnitObsolete = "Thermal Cracking Unit" not in refineryEquipment

 

print("Is Hydrotreating Unit installed?", IsUnitInstalled)
print("Is Thermal Cracking Unit obsolete?", IsUnitObsolete)


# In[89]:


#a. Access and print the details of the first employee in the list.
employees = [
    "John Doe, Senior Geologist, Geology, johndoe@email.com, 123-456-7890",
    "Jane Smith, Drilling Engineer, Drilling, janesmith@email.com, 987-654-3210",
    "Bob Johnson, Reservoir Engineer, Reservoir Engineering, bobjohnson@email.com, 456-789-0123",
    "Alice Brown, Petrophysicist, Petrophysics, alicebrown@email.com, 789-012-3456"
]

print(employees[0])


# In[93]:


#b. Add a new employee to the end of the list.
employees.append("Eva Green, Drilling Technician, Drilling, evagreen@email.com, 111-222-3333")


# In[91]:


print(employees)


# # Selection statement

# In[94]:


age=20
if age>18:
    print("Eligible")
else:
    print("not eligible")


# In[ ]:


low_fuel_thresold=1000
critical_fuel_thresold=500
current_fuel_level=int(input("enter current fuel level")


# In[ ]:





# In[ ]:


if current_fuel_level<critical_fuel_thresold:
    print("Critical Fuel Level Reached. Take Immeditate Action")
elif current_fuel_level<low_fuel_thresold:
     print("Send_fuel_low alter")
else:
     print("continue fueling")  


# # Range 
# --To print the sequence of number
# --range(0,0

# In[3]:


n=range(9)


# In[4]:


for i in range(5,12):
    print(1)


# In[5]:


#range with parameter
#range(5)
#range(2,10)
#range(2,5,20)
for i in range(3,10):
    print(i)
for i in range(2,5,10):
    print(i)


# # Functions
# 1. zip functions

# In[ ]:


#use zip() to group the information of each oil and gas field together:

oil_gas_data = [
    ("Field A", "Texas", 500000),
    ("Field B", "Alaska", 800000),
    ("Field C", "North Sea", 300000),
    ("Field D", "Gulf of Mexico", 600000),
]


Feild_name,Location,reserve=zip(*oil_gas_data)
print(Feild_name)
print(reserve)


# In[2]:


#2. Enumerate()
l1 = ["eat", "sleep", "repeat"]
s1 = "travel"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:", type(obj1))
print (list(enumerate(l1)))
 


# In[ ]:


#counter function
#we need to import a counter from the collection
count 

