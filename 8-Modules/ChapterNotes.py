#Chapter 8 - Modules!
#Chapter Notes -- 

#Programmers generally divide large programs into smaller pieces called modules.
#Modules are Python files with code in it - each one with a piece of a larger program.
#Python also has built-in modules.

#Importing Built-in Modules!
#To use a module, it must first be imported. To import use this syntax:

import[module_name]

#Once a module has been imported, variables and functions from it can be used.
#Here is how to import Python's math module.

import math

#Once a module has been imported, code from it can be used with the syntax:

import math

math.pow(2,3)

>> 8

#It's a best practice to import all modules at the top of your file.
#The random module is another built-in module. The function randint can generate
#a random integer: pass two parameters and it returns a random between them.

import random

random.randint(0,100)

>> 52

#The built-in statistics module can be used to calculate the mean, module, and
#mode in an iterable of numbers.

import statistics
nums = [1, 5, 33, 12, 46, 33, 2]

#mean
statistics.mean(nums)

#median
statistics.median(nums)

#mode
statistics.mode(nums)

>> 18.85
>> 12
>> 33

#The keyword module can check if a string is a Python keyword:

import keyword

keyword.iskeyword("for")
keyword.iskeyword("football")

>> True
>> False

#Importing other modules!
#Say you want to create a module, import it in another module, and use the code from it.
#See examples in tstp folder. 