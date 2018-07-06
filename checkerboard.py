# Write a program that prints a 'checkerboard' pattern to the console.

# Your program should require no input and produce console output that looks like so:

# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *


def checkerboard():
    lines = ""
    count = 0
    while count < 5:
        if count % 2 == 0:
            print ("* " * 8)
            count = count +1
        elif count % 2 != 0:
            print(" *" * 8)
            count = count + 1
    return lines

print(checkerboard())
