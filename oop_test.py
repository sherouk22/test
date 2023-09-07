#!/usr/bin/env python
# coding: utf-8

# In[4]:


class system():
    
    def __init__( self, name ,loan ,salary):
        self.name= name
        self.loan= loan
        self.salary= salary
    def customers(self):
        print("customers detils: ")
        print("name ", self.name)
        print("loan ", self.loan)
        print("salary ", self.salary)
        


# In[5]:


sherouk= system("sherouk" ,50000 ,5000)
sherouk.customers()


# In[ ]:





# In[6]:


class system_bank():
    
    def __init__( self, employee ,salary ,position):
        self.employee= employee
        self.salary= salary
        self.position= position
    def employees(self):
        print("employees detils: ")
        print("employee ", self.employee)
        print("salary ", self.salary)
        print("position ", self.position)


# In[8]:


ahmed= system_bank("ahmed" ,5000 ,"accountant")
ahmed.employees()


# In[ ]:




