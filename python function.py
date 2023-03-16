Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def avg(num1,num2,num3):
...     avg=(num1+num2+num3)/3
...     return (avg)
... 
>>> average= avg(37,108,67)
>>> print(avaerage)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(avaerage)
NameError: name 'avaerage' is not defined. Did you mean: 'average'?
>>> print(average)
70.66666666666667
>>> def avg(num1,num2,num3):
...     avg=(num1+num2+num3)/3
...     return (avg)
... 
>>> result=avg(num1,num2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    result=avg(num1,num2)
NameError: name 'num1' is not defined
>>> def avg(num1,num2,num3):
...     avg=(num1+num2+num3)/3
...     return (avg)
... 
>>> result=avg(37,108)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    result=avg(37,108)
TypeError: avg() missing 1 required positional argument: 'num3'
>>> def avg(num1,num2,num3):
...     avg=(num1+num2+num3)/3
...     return (avg)
... 
>>> avg(37,108,67)
70.66666666666667
>>> def avg(num1,num2,num3):
...     avg=(num1+num2+num3)/3
...     return (avg)
... 
>>> result=avg(37+108+67)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    result=avg(37+108+67)
TypeError: avg() missing 2 required positional arguments: 'num2' and 'num3'
def avg(num1,num2,num3):
    avg=(num1+num2+num3)/3
    return (avg)

print(avg(37,108,67))
70.66666666666667
def types(value):
    print(float(value))
    print(int(value))

    
types(3.24)
3.24
3

def squared(number):
    return (number**2)

squared(64)
4096

def int_to_string(number):
    retuen str(number)
    
SyntaxError: invalid syntax
def int_to_string(number):
    retuen str(number)
    
SyntaxError: invalid syntax
def int_to_string(number):
    retuen (number)

    
int_to_string(99)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int_to_string(99)
  File "<pyshell#37>", line 2, in int_to_string
    retuen (number)
NameError: name 'retuen' is not defined
