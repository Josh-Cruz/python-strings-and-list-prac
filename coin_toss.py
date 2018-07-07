# Write a function that simulates tossing a coin 5, 000 times. Your function should print how many times the head/tail appears.

# Sample output should be like the following:

# Starting the program...
# # 1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt
# # 2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt
# # 3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt
# # 4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# Attempt
# ...
# # 5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
# Attempt
# Ending the program, thank you!
# Hint: Use the python built-in round function to convert that floating point number into an integer

def coin_toss():
    import random
    x=0
    heads = 0
    tails = 0
    while x <= 5000:
        print "This is Flip number", x, "Flipping Now..."
        random_num = random.random()
        r_num = random_num * 100
        if r_num % 2 != 0:
           heads +=1
           print "It's Heads!", "Got", heads, " Head(s)so far and", tails, "Tail(s) so far."
           x+=1 
        else:
            tails+= 1
            print "It's Teads!", "Got", heads, " Head(s)so far and", tails, "Tail(s) so far."
            x+=1 
    return heads, tails

print(coin_toss())
