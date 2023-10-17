# Function to calculate the circumference of a circle
def circumference_of_circle(radius):
    if isinstance(radius, (int, float)):
        return 2 * 3.141592653589793 * radius

# Function to count the number of occurrences of a character in a string
def count_char_occurrences(string, char):
    if isinstance(string, str) and isinstance(char, str) and len(char) == 1:
        return string.count(char)

# Function to calculate the percentage of a number
def calculate_percentage(number, percentage):
    if isinstance(number, (int, float)) and isinstance(percentage, (int, float)):
        return (percentage / 100) * number

# Function to find the absolute difference between two numbers
def absolute_difference(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        return abs(num1 - num2)

# Function to capitalize the first letter of a string
def capitalize_first_letter(string):
    if isinstance(string, str):
        return string.capitalize()

# Function to calculate the square of a number
def square(number):
    if isinstance(number, (int, float)):
        return number ** 2

# Function to find the maximum of two numbers
def max_of_two(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        if num1 > num2:
            return num1
        else:
            return num2

# Function to calculate the square root of a number
def square_root(number):
    if isinstance(number, (int, float)) and number >= 0:
        return number ** 0.5

# Function to find the length of a string
def length(input_data):
    if isinstance(input_data, str):
        return len(input_data)


#HW7
radius=float(input("Enter the radius of the circle: "))
circumfrence=circumference_of_circle(radius)
print(f"{circumfrence:.2f}")


#HW8
string=input("Enter a string: ")
character=input("Enter a character: ")
a=count_char_occurrences(string,character)
print(f"The character occurs{a} times in the string.")

#HW9
number=float(input("Enter a number: "))
percentage=float(input("Enter a percentage: "))
crazy=calculate_percentage(number,percentage)
print(f"{percentage}% of {number} is {crazy:.2f}.")

#HW10
h=float(input("Enter a number: "))
l=float(input("Enter another number: "))
pk=absolute_difference(h,l)
print(f"The absolute diffrence is {pk:.2f}")


