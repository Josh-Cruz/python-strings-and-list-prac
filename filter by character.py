# # input
word_list = ['hello', 'world', 'my', 'name', 'is', 'Anna']
char = 'o'
# # output
# new_list = ['hello', 'world']

def filter_by_char(x,y):
    new_list = []
    for z in x:
        for c in z:
            if c == y:
                new_list.append(z)
            else:
                pass    
    print new_list

print (filter_by_char(word_list, char))