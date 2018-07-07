# Assignment: Stars
# Write the following functions.

# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out * .

# For example:

# x = [4, 6, 1, 3, 5, 7, 25]
# draw_stars(x) should print the following when invoked:

# ****
# ******
# *
# ***
# *****
# *******
# *************************
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(arr):
    for y in arr:
        if isinstance(y,int):
            print "*" * y
        else:
            for z in y[0]:
                print z.lower() * len(y)
        
print(draw_stars(x))

# Part II
# Modify the function above. Allow a list containing integers 
# and strings to be passed to the draw_stars() function. 
# When a string is passed, instead of displaying *, 
# display the first letter of the string according to
#  the example below. You may use the .lower() string method for this part.

# For example:


# draw_stars(x) should print the following in the terminal:

# ****
# ttt
# *
# mmmmmmm
# *****
# *******
# jjjjjjjjjjj
