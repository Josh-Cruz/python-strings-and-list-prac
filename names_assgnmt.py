# Write the following function.

# Part I
# Given the following list:

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# Create a program that outputs:

# Michael Jordan
# John Rosales
# Mark Guillen
# KB Tonel

users = {
    'Students': [
        {'first_name':  'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'}
    ]
}

# def name_maker(dict):
#     x = 0
#     while x < len(dict):
#         print dict[x]['first_name'] + " " + dict[x]["last_name"]
#         x +=1

# print(name_maker(users))


# print users[0[1]]

def name_maker(dictionary):
    count = 1
    z = 0
    # v = 0
    for x, y in dictionary.items():
        print x
        z = 0
        count = 1
        # print y
        while z < len(y):
            length = len(y[z]['first_name'] + y[z]['last_name'])
            print count, y[z]['first_name'] + " " + y[z]['last_name'], length
            z +=1
            count += 1
        
            


        
    
        

print(name_maker(users))

# Part II
# Now, given the following dictionary:


# Create a program that prints the following format(including number of characters in each combined name):

# Students
# 1 - MICHAEL JORDAN - 13
# 2 - JOHN ROSALES - 11
# 3 - MARK GUILLEN - 11
# 4 - KB TONEL - 7
# Instructors
# 1 - MICHAEL CHOI - 11
# 2 - MARTIN PURYEAR - 13
