#!/usr/bin/env python
# coding: utf-8
1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.Ans :*:expression'hello':value-87.8 :value- :expression/ :expression+ :expression6 :value2. What is the difference between string and variable?Ans : A variable is a reference to the value stored in the memory . A string is a datatype which allows to store characters various operations such as append , length using inbuilt functions.String is immutable datatype.3. Describe three different data types.Ans:
List is a datatype that stores values in either homogenous or heterogenous manner.It is denoted using [] brackets
eg: l=[1,2,'def',True].List is mutable datatype

Tuple is similar to list,it also stores values in either homogenus or heterogenous manner.It is denoted using () brackets.Tuple is immutable datatype
eg:t=(3,7,'fer',3+5j)

Complex datatype has two parts ie ,real and imaginary.Imaginary part is always denoted with j.The value of square of j is -1,It has in built functions such as conjugate , real and imag
eg:8+6j4. What is an expression made up of? What do all expressions do?Ans:An expression is made up of either operators, literals or variables.Expressions are representations of values.5. This assignment statements, like spam = 10. What is the difference between an
expression and a statement?Ans:A statement is an instruction followed by the interpreter whereas an expression is combination of variables,operators and values that evaluates and returns the results6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1
# In[2]:


bacon=22


# In[3]:


bacon+1


# In[4]:


bacon

The variable bacon contains value 22 because after executing the expression bacon+1 it is not assigned back to bacon.Hence bacon=227. What should the values of the following two terms be?
'spam' + 'spamspam'
'spam' * 3
# In[5]:


'spam'+'spamspam'


# In[6]:


'spam' *3

8. Why is eggs a valid variable name while 100 is invalid?Ans: eggs is a sequence of characters whereas 100 is series of digits.Python doesnt accept digits entirely in variable name9. What three functions can be used to get the integer, floating-point number, or string
version of a value?
# In[7]:


int(4.5)


# In[8]:


float(3)


# In[9]:


str(3+8j)

10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos '
# In[10]:


'I have eaten ' + 99 + ' burritos '

This expression causes error because it tries to concatenate str and int values, It can be corrected by changing the int value to string
# In[11]:


'I have eaten ' + '99' + ' burritos '


# In[ ]:




