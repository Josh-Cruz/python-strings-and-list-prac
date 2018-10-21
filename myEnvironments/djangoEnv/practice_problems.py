# a_list = ["item1" , "item2", "item3"]

# # print(a_list)

# b_list = [232,55,710,1]

# # for elm in b_list:
# #     sum = elm
# #     sum =  sum + elm 
# # print("sum is " + str(sum))



# # for i in range(len(a_list)):
# #     print(b_list[i])

# arr = [18,234,35,48,85]
# arr1 = [3,5,5,1]
# arr2 = [3,2,2,2]
# arr3 = []
# arr4 = [12]

# # loop through each elm in arr
# # declare 2 vars largest & second_largest
# # if index is currently larger than largest it becomes largest and the curr val of 2lg gets pushed to 2nd largest
# # else if index is larger than  2nd largest it becomes 2nd largest
# #  if empty return none

# def findsecondlargest(arr):
#     largest = 0
#     second_largest = 0
#     if len(arr) == 0:
#             print("empty array")
#             return None
#     elif len(arr) == 1:
#             print ("only one entry in array")
#             return largest
#     else:    
#         largest = arr[0]
#         for elm in arr:
#             if elm > largest:
#                 second_largest = largest
#                 largest = elm
#                 print "second largest is: ", second_largest        

# # findsecondlargest(arr)
            

# str1 = "ABC"
# str2 = "CBAd"



# def are_reverse(strg1, strg2):
#     i = 0
#     count = 1
#     for j  in reversed(range(len(strg2))):
#         if strg2[j] != strg1[i]:
#             print "Strings Don't Match"
#             return False
#         else:
#             print count , "Time(s) around"
#             print "string 1: ", strg1[i]
#             print "string 2: " ,strg2[j]
#             count+=1
#             i = i +1
#     return True

# # are_reverse(str1, str2)
        
# def larger_than(str1, str2):
#     i = 0
#     for item in str1:
#         if str2[i] > str1[i]:
#             print "its not GT"
#             return False
#         elif str2[i] == str1[i]:
#             print "string 1: ", str1[i]
#             print "string 2: " , str2[i] 
#             i += 1
#         else:
#             print str1 , "is actually greater than", str2
#             return True
#     print "the numbers are the same "        
#     return False        

# num1 = "999"
# num2 = "2468"         

# # larger_than(num1,num2)
        
# list_2d = [ [0,0,0,1,0],
#             [0,0,0,0,0],
#             [1,0,0,1,0],
#             [0,0,0,0,1],
#             [0,0,0,1,1]]


# def rooks_are_safe(list):
#     coordinates={}
#     row_count = 0
#     for row in list:
#         row_count = row_count + 1
#         if sum(row)== 0:
#             print "skipped a row"
#             pass
#         else:
#             print "row: ", row_count
#             for column in range(len(row)):
#                 if row[column] == 1:
#                     if row_count in coordinates:
#                         print "rooks are not safe"
#                         return False
#                     elif column in coordinates.values():
#                         print "rooks are not safe"
#                         return False
#                     else:
#                         coordinates[row_count] = column
#     print "rooks are safe!"
#     return True 



# # rooks_are_safe(list_2d)

# list_neg = [ [-4,-3,-2,-1],
#             [-3,-2,-1,0],
#             [-2,-1,0,1],
#             [-1,0,0,0]
#         ]

# # def find_neg(list):
# #     neg_sum = 0
# #     for row in list:
# #         for item in row:
# #             if item < 0:
# #                 neg_sum += item
# #             else:
# #                 continue
# #     print (neg_sum)


# # find_neg(list_neg)


# my_list = [2,3,1,4,9]

# def add_upto_ten(list):
#     numbers = {}
#     for i in range(len(list)):
#         remainder = 10 - list[i]
#         if remainder in numbers.values():
#             print remainder, list[i]
#             return
#         else:
#             numbers[remainder] = list[i]
#             print numbers
#     print "nothing equalled ten, sorry!"

# add_upto_ten(my_list)    

# def rotLeft(a, d):
#     temp = 0
#     for num in range(len(a)):
#         temp = num
#         a.pop(a[num])
#         push(temp, a)


arr = [2,4,3,1,5]

def min_max_avg(array):
    sum_arr = 0
    result = {
        'max_num': array[0],
        'min_num': array[0]
    }
    for num in array:
        if num > result['max_num']:
            result['max_num'] = num
        elif num < ['min_num']:
            result['min_num'] = num
        sum_arr += num

    result['avg'] = sum_arr / len(array)
    print result
    return result 


# min_max_avg(arr)

#  increment = traveled[dir] + 1
#             traveled[dir] = increment 
#             if dir in traveled:

def isValidWalk(walk):
    traveled = {}
    if len(walk) > 10:
        return False
    else:
        for direction in walk:
            traveled[direction] = +1    
            if direction == "n":
                if  "s" in traveled and traveled["s"] > 0:
                    traveled[direction] = 0
                    traveled["s"] = traveled["s"] -1
            elif direction == "s":
                if  "n" in traveled  and traveled["n"] > 0:
                    traveled[direction] = 0
                    traveled["n"] = traveled["n"] -1
            elif direction == "e":
                if  "w" in traveled  and traveled["w"] > 0:
                    traveled[direction] = 0
                    traveled["w"] = traveled["w"] -1
            elif direction == "w":
                if  "e" in traveled and traveled["e"] > 0:
                    traveled[direction] = 0
                    traveled["e"] = traveled["e"] -1
    if 0 not in traveled.keys():
        return False
    else:
        return True
            
print isValidWalk(["w", "e", "s", "e", "s", "e", "w", "n", "w", "n"])