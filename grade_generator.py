# Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A
# The result should be like this:

def grade_gen ():
    x =0
    
    import random
   
    while x <= 10:
        random_num = random.random()
        r_num = random_num * 100
        if r_num <= 59:
            print int(r_num), "is your grade", "you failed..."
            x+=1
        elif r_num <= 69:
            print int(r_num), "is your grade", "'D'eed you really think you did well?"
            x+=1
        elif r_num <= 79:
            print int(r_num), "is your grade", " 'C' you ain't so bad..."
            x+=1
        elif r_num <= 89:
            print int(r_num), "is your grade", "you gots a B"
            x+=1
        elif r_num > 89:
            print int(r_num), "is your grade", "WHOA Over Achiever...."
            x+=1
            
print(grade_gen())
