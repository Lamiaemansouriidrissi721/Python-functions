#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#def function_name(parameters):
    # Code inside the function
    #result = some_calculation(parameters)
    #return result


# In[ ]:


Exercices 1:Calculate Area of a Rectangle
Write a function that takes the length and width of a rectangle as parameters and returns its area.


# In[5]:


def r_area (length, width):
    the_area_of_a_rectangle = length * width 
    return the_area_of_a_rectangle
x = r_area (15,7)
print(x)


# In[ ]:


Exercise 2: Celsius to Fahrenheit Conversion

Write a function that converts a temperature in Celsius to Fahrenheit. 
The formula is: Fahrenheit = (Celsius * 9/5) + 32.


# In[8]:


def celsius_convr (celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius_to_fahrenheit=celsius_convr(18)
print('the convereted temperature is :'+' '+str (celsius_to_fahrenheit))


# In[ ]:


Exercise 3: Check Even or Odd

Write a function that takes an integer as input and returns whether it's even or odd.


# In[3]:


def integerorodd(integer):
    if i% 2 ==0:
        return 'even '
    else :
        return 'odd' 
i=int (input('write a number :'))
result =integerorodd(i)
print (result)


# In[ ]:


Exercise 4: Maximum of Three Numbers

Write a function that takes three numbers as parameters and returns the maximum of the three.


# In[8]:


import random

def numbers():
    max_numbers = max(range(10))
    return max_numbers

y = numbers()
print('The maximum of the numbers: ' + str(y))


# In[ ]:


#another way 
import random

def numbers():
    random_numbers = [random.randint(1, 10) for _ in range(10)]
    max_number = max(random_numbers)
    return max_number

y = numbers()
print('The maximum of the numbers:', y)


# In[ ]:


Exercise 5: Count Characters in a String

Write a function that takes a string as input and returns the count of characters in the string.


# In[10]:


def string_count (sentence):
    count_str= len(sentence)
    return count_str
s=string_count(str(input('write a sentence')))
s


# In[ ]:




