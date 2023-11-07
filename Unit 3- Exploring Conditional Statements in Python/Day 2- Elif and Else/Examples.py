# number_grade = 76

# if number_grade >= 80:
#     print("A")
# if number_grade >= 70:
#     print ("B")
# if number_grade >= 60:
#     print ("C")
# #if number_grade >= 50:
#     #print ("D")
# #if number_grade <= 50:
#     #print ("F")

#These are all seperate if statements so they each run seperetly
#prints B, C, D on seperate lines because 3 conditions were true

#The Folowing code has 5 seperate if statements - evaluates 5 conditions
# number_grade = 76

# if number_grade >= 80:
#     print("A")
# if 70 <= number_grade < 80:
#     print ("B")
# if 60 <= number_grade < 70:
#     print ("C")
# if 50 <= number_grade < 60:
#     print ("D")
# if  number_grade < 50:
#     print ("F")

#prints B (Works as intended)


# number_grade = 76

# if number_grade >= 80:
#     print("A")
# elif number_grade >= 70:
#     print ("B")
# elif number_grade >= 60:
#     print ("C")
# elif number_grade >= 50:
#     print ("D")
# elif number_grade <= 50:
#     print ("F")




# number_grade = 76

# if number_grade >= 80:
#     print("A")
# elif number_grade >= 70:
#     print ("B")
# elif number_grade >= 60:
#     print ("C")
# elif number_grade >= 50:
#     print ("D")
# else:
#     print ("F")



def inspect_number(x):
    if x > 0:
        print ("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")

inspect_number(7)