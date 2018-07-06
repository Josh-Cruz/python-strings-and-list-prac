# Odd/Even:
# Create a function called odd_even that counts from 1 to 2000.
#  As your loop executes have your program print the number of 
# that iteration and specify whether it's an odd or even number.

# Your program output should look like below:

# Number is 1.  This is an odd number.
# Number is 2.  This is an even number.
# Number is 3.  This is an odd number.
# ...
# Number is 2000.  This is an even number

def odd_even():
    x = 0
    while x <= 2000:
        if x % 2 == 0:
            print "number is", x,"This Number is Even"
            x= x + 1
        elif x % 2 != 0:
            print "number is", x,"This Number is Odd"
            x = x + 1
           
# print (odd_even())
# 
# Multiply:
# Create a function called 'multiply' that iterates through
#  each value in a list (e.g. a = [2, 4, 10, 16]) and returns
#  a list where each value has been multiplied by 5.

# The function should multiply each value in the 
# list by the second argument. For example, let's say:

# a = [2,4,10,16]
# Then:

# b = multiply(a, 5)
# print b
# Should print [10, 20, 50, 80 ].


a = [2, 4, 10, 16]

def multiply(x,y):
    for z in range(len(x)):
        x[z] = x[z] * y
    return x

b = multiply(a, 5)
print b

# Hacker Challenge:
# Write a function that takes the multiply function call as an argument. 
# Your new function should return the multiplied list as a two-dimensional list.
#  Each internal list should contain the 1's times the number in the original list.
#  Here's an example:

def layered_multiples(func):
    new_array = []
    for x in func:    
        new_array.append([1]*x) 
    return new_array
        

 
x = layered_multiples(multiply([2,4,5],3))
print x
# # output
# >>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
