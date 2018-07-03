# Assignment: String and List Practice
# Use only the built-in methods and functions from the previous tabs to do the following exercises.
# You will find the following methods and functions useful:

#  .find()

#  .replace()

#  min()

#  max()

#  .sort()

#  len()

# Find and Replace
# In this string: words = "It's thanksgiving day. It's my birthday,too!" print the position of the first instance of the word "day". 
# Then create a new string where the word "day" is replaced with the word "month".

# words = "It's thanksgiving day. It's my birthday,too!"
# print words.replace("day", "month",1)
# Solved






# Min and Max
# Print the min and max values in a list like this one: x = [2, 54, -2, 7, 12, 98].
#  Your code should work for any list.


# x = [2, 54, -2, 7, 12, 98]
# min = 0
# max = 0
# for num in x:
#     if min > num:
#         min = num
#     elif max < num:
#         max = num
# print (min, " is the minimum")
# print (max, " Is The Maximum")  
#solved


# First and Last
# Print the first and last values in a list like this one:
#  x = ["hello", 2, 54, -2, 7, 12, 98, "world"]. Now create a new list containing
#  only the first and last values in the original list. Your code should work for any list.
# x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
# print x[0]
# print x[-1]
# Solved


# New List
# Start with a list like this one: x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
# . Sort your list first. Then, split your list in half.
#  Push the list created from the first half to position 0 of the list created from the 
# second half. The output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]. Stick with it, this one is tough!

x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]

x.sort()
y = x[:len(x)/2]
x[0] = y
print x


