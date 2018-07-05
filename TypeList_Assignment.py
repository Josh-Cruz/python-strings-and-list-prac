
# #input
l = ['magical unicorns', 19, 'hello', 98.98, 'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"

# # input
# l = [2, 3, 1, 7, 4, 12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"

# # input
# l = ['magical', 'unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"

def typecheck(param):
    sums = 0
    strings = ""
    for x in param:
        if isinstance(x, int):
            sums += x
        elif isinstance(x, str):
            strings += x
    if str(sums) != "" and strings == "":
        print "the sum is:", sums
        print "The list you entered is of the integer Type"
    elif sums == 0 :
        print"the strings smushed together are:", strings
        print "The list you entered is a bunch of strings"
    elif str(sums) != "" and strings != "":
        print "the sum is:", sums
        print "the strings smushed together are:" , strings
        print "The list you entered is a mixed Type"
    
    
print(typecheck(l))    


# old way that dint work
# 
# if isinstance(param, (list, int)):
#         for x in param:
#             sums += x
#         print "the sum is:", sums
#         print "The list you entered is of the integer Type"
#     elif isinstance(param, (list, tuple)):
#         for x in param:
#             if isinstance(x, int):
#                 sums += int(x)
#             elif isinstance(x, str):
#                 strings += str(x)
            
#         print "the sum is:", sums
#         print "the strings smushed together are:" , strings
#         print "The list you entered is a mixed Type"
#     elif isinstance(param, (list,str)):
#         for x in param:
#             strings += x
#         print "the strings smushed together are:", strings
#         print param
#         print "The list you entered is of the string Type"
