# Assignment: Dictionary in, tuples out
# Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:

#     # function input
my_dict = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}
# #function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def dict_to_tuple(dictn):
   print dictn.items()
    # print [(v, k) for v, k in dictn.iteritems()]


    
    
    # new_dict = {}
    # for x in dictn:
    #     for y in dictn:
    #        print new_dict[x].append((y))

print(dict_to_tuple(my_dict))
