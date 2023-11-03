# Check if a number is positive.
number = int(input("Please enter a number: "))
if number > 0:
    print(f"{number} is positive")
if number <= 0:
    print(f"{number} is not positive")

#Determine if a person can vote (18 or older).
age = int(input("Please enter your age: "))

if age >= 18:
    print("You are eligable to vote")

if age < 18:
    print("You are not eligable to vote")

#Please Enter a string
str = input("Please enter a String: ")
if len(str) == 0:
    print("The String is Empty")

if len(str) !=0:
    print("The String is not empty ")

#Write a function that returns the maximum of two numbers.
def max_number(a, b):
    if a < b:
        return a
    
    return b


print(max_number(14,5))
print(max_number(5,14))

#Check if a user's input is equal to a secret password
def password_checker(password, user_input):
    if password == user_input:
        return True
    
    return False

print(password_checker("fhdj","ie"))

#Write a function that checks if a number is within a specific range (1-10 inclusive, lower-upper)

def range_checker(num, lower, upper):
    if lower <=num <=upper:
        return True
    return False

a = int(input("Please enter a number between 1-10: "))
print(range_checker(a,1,10))
if range_checker(a, 1, 10):
    print("W person")

if range_checker(a,1,10) == False:
    print("You suck")

 #Write a function that accepts a numerical grade and returns the Letter Grade.

def grade_converter(grade):
    if grade >= 80:
        return "A"
    if grade >= 70:
        return "B"
    if grade >= 60:
        return "C"
    if grade >= 50:
        return "Fail"