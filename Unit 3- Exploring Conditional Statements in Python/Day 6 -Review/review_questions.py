#1
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("number is even.")

else:
    print("number is odd.")

#2
str = input("Enter a word: ")

if len(str) < 3:
    print(str)
else:
    print(str[len(str)-3:len(str)])

#3
number = int(input("Enter a number between 1-10: "))

if not 1 <= number <= 10:
    print("invalid input")

else:
    print("All good")

#4
number = int(input("Enter a number: "))
if number**6 > 1000:
    print("The number is greater than 1000 when raised to the power of 6.")

else:
    print("The number is not greater than 1000 when raised to the power of 6.")

#5
def number_function(number, outside_mode):
    if outside_mode and (number <= 1 or number > 10):
        return True
    
    
    elif not outside_mode and 1 <= number <= 10:
        return True
    
    else:
        return False

print(number_function(4, True))

#6
str1 = 'dababy'
if len(str1) < 2:
    print(str1)
else:
    print(str1[:2])

#7
number1 = int(input("Enter a number: "))
def positive_checker(number1):
    if number1 > 0:
        return "Number is greater than 0"
    
    else:
        return "Number is 0"
    
print(positive_checker(number1))